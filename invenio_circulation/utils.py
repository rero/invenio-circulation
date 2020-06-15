# -*- coding: utf-8 -*-
#
# Copyright (C) 2018-2020 CERN.
# Copyright (C) 2018-2020 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Circulation API."""


import arrow

from .errors import NotImplementedConfigurationError


def patron_exists(patron_pid):
    """Return True if patron exists, False otherwise."""
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_PATRON_EXISTS"
    )


def item_exists(item_pid):
    """Return True if item exists, False otherwise.

    :param item_pid: a dict containing `value` and `type` fields to
        uniquely identify the item.
    """
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_ITEM_EXISTS"
    )


def document_exists(document_pid):
    """Return True if document exists, False otherwise."""
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_DOCUMENT_EXISTS"
    )


# NOTE: Its on purpose `ref` and not `$ref` so it doesn't try to resolve
def item_ref_builder(loan_pid, loan):
    """Return the $ref for item_pid."""
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_ITEM_REF_BUILDER"
    )


# NOTE: Its on purpose `ref` and not `$ref` so it doesn't try to resolve
def patron_ref_builder(patron_pid, loan):
    """Return the $ref for patron_pid."""
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_PATRON_REF_BUILDER"
    )


# NOTE: Its on purpose `ref` and not `$ref` so it doesn't try to resolve
def document_ref_builder(document_pid, loan):
    """Return the $ref for document_pid."""
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_DOCUMENT_REF_BUILDER"
    )


def item_location_retriever(item_pid):
    """Retrieve the location pid of the passed item pid.

    :param item_pid: a dict containing `value` and `type` fields to
        uniquely identify the item.
    """
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_ITEM_LOCATION_RETRIEVER"
    )


def item_can_circulate(item_pid):
    """Return if item is available for checkout.

    :param item_pid: a dict containing `value` and `type` fields to
        uniquely identify the item.
    """
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_POLICIES.checkout.item_can_circulate"
    )


def can_be_requested(loan):
    """Should return True if document or item can be requested."""
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_POLICIES.request.can_be_requested"
    )


def get_default_loan_duration(loan, initial_loan):
    """Return a default loan duration in timedelta.

    :param loan: the current loan to extend, updated with transition params
    :param initial_loan: the loan before applying transition params
    """
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_POLICIES.checkout.duration_default"
    )


def is_loan_duration_valid(loan):
    """Validate the loan duration."""
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_POLICIES.checkout.duration_validate"
    )


def get_default_extension_duration(loan, initial_loan):
    """Return a default extension duration in timedelta.

    :param loan: the current loan to extend, updated with transition params
    :param initial_loan: the loan before applying transition params
    """
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_POLICIES.extension.duration_default"
    )


def get_default_extension_max_count(loan):
    """Return a default extensions max count."""
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_POLICIES.extension.max_count"
    )


def transaction_location_validator(transaction_location_pid):
    """Validate that the given transaction location PID is valid.

    :param transaction_location_pid: the transaction location PID sent with
        the REST request.
    """
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_TRANSACTION_LOCATION_VALIDATOR"
    )


def transaction_user_validator(transaction_user_pid):
    """Validate that the given transaction user PID is valid.

    :param transaction_user_pid: the transaction user PID sent with
        the REST request.
    """
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_TRANSACTION_USER_VALIDATOR"
    )


def str2datetime(str_date):
    """Parse string date with timezone and return a datetime object."""
    return arrow.get(str_date).to('utc')


def validate_item_pickup_transaction_locations(loan, destination, **kwargs):
    """Validate the loan item, pickup and transaction locations.

    This also allow for extra validation if needed at the library level.

    :param loan: the loan
    :param destination: the destination of the loan

    :return: False if validation is not possible, otherwise True
    """
    raise NotImplementedConfigurationError(
        config_variable="CIRCULATION_LOAN_LOCATIONS_VALIDATION"
    )
