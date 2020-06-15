# -*- coding: utf-8 -*-
#
# Copyright (C) 2018-2020 CERN.
# Copyright (C) 2018-2020 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Tests for loan states."""

import pytest

from invenio_circulation.errors import NotImplementedConfigurationError, \
    NoValidTransitionAvailableError
from invenio_circulation.proxies import current_circulation
from invenio_circulation.utils import \
    validate_item_pickup_transaction_locations

from .helpers import SwappedConfig


def test_validate_pickup_transaction_locations_not_implemented(
        loan_created, params):
    """Test transition from PENDING to ITEM_AT_DESK.

    when the method validate_item_pickup_transaction_locations is not
    implemented, a NotImplementedConfigurationError is raised.
    """
    loan = current_circulation.circulation.trigger(
        loan_created,
        **dict(
            params,
            trigger="request",
            pickup_location_pid="pickup_location_pid",
        )
    )
    assert loan["state"] == "PENDING"

    with pytest.raises(NotImplementedConfigurationError):
        with SwappedConfig(
            "CIRCULATION_LOAN_LOCATIONS_VERIFICATIONS",
                validate_item_pickup_transaction_locations(
                    loan, "ITEM_AT_DESK")
        ):
            loan = current_circulation.circulation.trigger(
                loan, **dict(params)
            )


def test_validate_item_at_desk(loan_created, params):
    """Test transition from PENDING to ITEM_AT_DESK state."""

    loan = current_circulation.circulation.trigger(
        loan_created,
        **dict(
            params,
            trigger="request",
            pickup_location_pid="pickup_location_pid",
        )
    )
    assert loan["state"] == "PENDING"

    with SwappedConfig(
        "CIRCULATION_ITEM_LOCATION_RETRIEVER", lambda x: "pickup_location_pid"
    ):
        loan = current_circulation.circulation.trigger(
            loan, **dict(params)
        )
        assert loan["state"] == "ITEM_AT_DESK"


def test_validate_item_in_transit_pickup(loan_created, params):
    """Test transition from PENDING to ITEM_IN_TRANSIT_FOR_PICKUP state."""

    loan = current_circulation.circulation.trigger(
        loan_created,
        **dict(
            params,
            trigger="request",
            pickup_location_pid="pickup_location_pid",
        )
    )
    assert loan["state"] == "PENDING"

    with SwappedConfig(
        "CIRCULATION_ITEM_LOCATION_RETRIEVER", lambda x: "pickup_location_pid"
    ):
        loan = current_circulation.circulation.trigger(
            loan, **dict(params,
                         pickup_location_pid="other_location_pid")
        )
        assert loan["state"] == "ITEM_IN_TRANSIT_FOR_PICKUP"


def test_checkout_without_item_attached(loan_created, params):
    """Test checkout on PENDING LOAN without item_pid attached."""

    assert loan_created["state"] == "CREATED"

    with SwappedConfig(
        "CIRCULATION_ITEMS_RETRIEVER_FROM_DOCUMENT", lambda x: []
    ):
        loan = current_circulation.circulation.trigger(
            loan_created, **dict(params, trigger="request")
        )

        assert "item_pid" in loan
        assert "pickup_location_pid" in loan
        assert loan["state"] == "PENDING"

        del loan["item_pid"]
        del params["item_pid"]

        with pytest.raises(NoValidTransitionAvailableError):
            current_circulation.circulation.trigger(
                loan, **dict(params, trigger="next")
            )


def test_checkout_with_different_pickup_location(loan_created, params):
    """Test checkout with pickup location different than item location."""

    assert loan_created["state"] == "CREATED"

    with SwappedConfig(
        "CIRCULATION_ITEM_LOCATION_RETRIEVER", lambda x: "pickup_location_pid"
    ):
        loan = current_circulation.circulation.trigger(
            loan_created, **dict(params, trigger="request",
                                 pickup_location_pid="pickup_location_pid")
        )

        assert loan["item_pid"] == dict(type="itemid", value="item_pid")
        assert loan["pickup_location_pid"] == "pickup_location_pid"
        assert loan["state"] == "PENDING"

        current_circulation.circulation.trigger(
            loan, **dict(params, trigger="next",
                         pickup_location_pid="other_location_pid")
        )

        assert loan["state"] == "ITEM_IN_TRANSIT_FOR_PICKUP"


def test_checkout_with_same_pickup_location(loan_created, params):
    """Test checkout with pickup location same as item location."""

    assert loan_created["state"] == "CREATED"

    with SwappedConfig(
        "CIRCULATION_ITEM_LOCATION_RETRIEVER", lambda x: "pickup_location_pid"
    ):
        loan = current_circulation.circulation.trigger(
            loan_created, **dict(params, trigger="request",
                                 pickup_location_pid="pickup_location_pid")
        )

        assert loan["item_pid"] == dict(type="itemid", value="item_pid")
        assert loan["pickup_location_pid"] == "pickup_location_pid"
        assert loan["state"] == "PENDING"

        current_circulation.circulation.trigger(
            loan, **dict(params, trigger="next",
                         pickup_location_pid="pickup_location_pid")
        )

        assert loan["state"] == "ITEM_AT_DESK"
