# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class V1Payment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, merchant_id=None, created_at=None, creator_id=None, device=None, payment_url=None, receipt_url=None, inclusive_tax_money=None, additive_tax_money=None, tax_money=None, tip_money=None, discount_money=None, total_collected_money=None, processing_fee_money=None, net_total_money=None, refunded_money=None, swedish_rounding_money=None, gross_sales_money=None, net_sales_money=None, inclusive_tax=None, additive_tax=None, tender=None, refunds=None, itemizations=None):
        """
        V1Payment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'merchant_id': 'str',
            'created_at': 'str',
            'creator_id': 'str',
            'device': 'Device',
            'payment_url': 'str',
            'receipt_url': 'str',
            'inclusive_tax_money': 'V1Money',
            'additive_tax_money': 'V1Money',
            'tax_money': 'V1Money',
            'tip_money': 'V1Money',
            'discount_money': 'V1Money',
            'total_collected_money': 'V1Money',
            'processing_fee_money': 'V1Money',
            'net_total_money': 'V1Money',
            'refunded_money': 'V1Money',
            'swedish_rounding_money': 'V1Money',
            'gross_sales_money': 'V1Money',
            'net_sales_money': 'V1Money',
            'inclusive_tax': 'list[V1PaymentTax]',
            'additive_tax': 'list[V1PaymentTax]',
            'tender': 'list[V1Tender]',
            'refunds': 'list[V1Refund]',
            'itemizations': 'list[V1PaymentItemization]'
        }

        self.attribute_map = {
            'id': 'id',
            'merchant_id': 'merchant_id',
            'created_at': 'created_at',
            'creator_id': 'creator_id',
            'device': 'device',
            'payment_url': 'payment_url',
            'receipt_url': 'receipt_url',
            'inclusive_tax_money': 'inclusive_tax_money',
            'additive_tax_money': 'additive_tax_money',
            'tax_money': 'tax_money',
            'tip_money': 'tip_money',
            'discount_money': 'discount_money',
            'total_collected_money': 'total_collected_money',
            'processing_fee_money': 'processing_fee_money',
            'net_total_money': 'net_total_money',
            'refunded_money': 'refunded_money',
            'swedish_rounding_money': 'swedish_rounding_money',
            'gross_sales_money': 'gross_sales_money',
            'net_sales_money': 'net_sales_money',
            'inclusive_tax': 'inclusive_tax',
            'additive_tax': 'additive_tax',
            'tender': 'tender',
            'refunds': 'refunds',
            'itemizations': 'itemizations'
        }

        self._id = id
        self._merchant_id = merchant_id
        self._created_at = created_at
        self._creator_id = creator_id
        self._device = device
        self._payment_url = payment_url
        self._receipt_url = receipt_url
        self._inclusive_tax_money = inclusive_tax_money
        self._additive_tax_money = additive_tax_money
        self._tax_money = tax_money
        self._tip_money = tip_money
        self._discount_money = discount_money
        self._total_collected_money = total_collected_money
        self._processing_fee_money = processing_fee_money
        self._net_total_money = net_total_money
        self._refunded_money = refunded_money
        self._swedish_rounding_money = swedish_rounding_money
        self._gross_sales_money = gross_sales_money
        self._net_sales_money = net_sales_money
        self._inclusive_tax = inclusive_tax
        self._additive_tax = additive_tax
        self._tender = tender
        self._refunds = refunds
        self._itemizations = itemizations

    @property
    def id(self):
        """
        Gets the id of this V1Payment.
        The payment's unique identifier.

        :return: The id of this V1Payment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1Payment.
        The payment's unique identifier.

        :param id: The id of this V1Payment.
        :type: str
        """

        self._id = id

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this V1Payment.
        The unique identifier of the merchant that took the payment.

        :return: The merchant_id of this V1Payment.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this V1Payment.
        The unique identifier of the merchant that took the payment.

        :param merchant_id: The merchant_id of this V1Payment.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def created_at(self):
        """
        Gets the created_at of this V1Payment.
        The time when the payment was created, in ISO 8601 format.

        :return: The created_at of this V1Payment.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this V1Payment.
        The time when the payment was created, in ISO 8601 format.

        :param created_at: The created_at of this V1Payment.
        :type: str
        """

        self._created_at = created_at

    @property
    def creator_id(self):
        """
        Gets the creator_id of this V1Payment.
        The unique identifier of the Square account that took the payment.

        :return: The creator_id of this V1Payment.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this V1Payment.
        The unique identifier of the Square account that took the payment.

        :param creator_id: The creator_id of this V1Payment.
        :type: str
        """

        self._creator_id = creator_id

    @property
    def device(self):
        """
        Gets the device of this V1Payment.
        The device that took the payment.

        :return: The device of this V1Payment.
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this V1Payment.
        The device that took the payment.

        :param device: The device of this V1Payment.
        :type: Device
        """

        self._device = device

    @property
    def payment_url(self):
        """
        Gets the payment_url of this V1Payment.
        The URL of the payment's detail page in the merchant dashboard. The merchant must be signed in to the merchant dashboard to view this page.

        :return: The payment_url of this V1Payment.
        :rtype: str
        """
        return self._payment_url

    @payment_url.setter
    def payment_url(self, payment_url):
        """
        Sets the payment_url of this V1Payment.
        The URL of the payment's detail page in the merchant dashboard. The merchant must be signed in to the merchant dashboard to view this page.

        :param payment_url: The payment_url of this V1Payment.
        :type: str
        """

        self._payment_url = payment_url

    @property
    def receipt_url(self):
        """
        Gets the receipt_url of this V1Payment.
        The URL of the receipt for the payment. Note that for split tender payments, this URL corresponds to the receipt for the first tender listed in the payment's tender field. Each Tender object has its own receipt_url field you can use to get the other receipts associated with a split tender payment.

        :return: The receipt_url of this V1Payment.
        :rtype: str
        """
        return self._receipt_url

    @receipt_url.setter
    def receipt_url(self, receipt_url):
        """
        Sets the receipt_url of this V1Payment.
        The URL of the receipt for the payment. Note that for split tender payments, this URL corresponds to the receipt for the first tender listed in the payment's tender field. Each Tender object has its own receipt_url field you can use to get the other receipts associated with a split tender payment.

        :param receipt_url: The receipt_url of this V1Payment.
        :type: str
        """

        self._receipt_url = receipt_url

    @property
    def inclusive_tax_money(self):
        """
        Gets the inclusive_tax_money of this V1Payment.
        The sum of all inclusive taxes associated with the payment.

        :return: The inclusive_tax_money of this V1Payment.
        :rtype: V1Money
        """
        return self._inclusive_tax_money

    @inclusive_tax_money.setter
    def inclusive_tax_money(self, inclusive_tax_money):
        """
        Sets the inclusive_tax_money of this V1Payment.
        The sum of all inclusive taxes associated with the payment.

        :param inclusive_tax_money: The inclusive_tax_money of this V1Payment.
        :type: V1Money
        """

        self._inclusive_tax_money = inclusive_tax_money

    @property
    def additive_tax_money(self):
        """
        Gets the additive_tax_money of this V1Payment.
        The sum of all additive taxes associated with the payment.

        :return: The additive_tax_money of this V1Payment.
        :rtype: V1Money
        """
        return self._additive_tax_money

    @additive_tax_money.setter
    def additive_tax_money(self, additive_tax_money):
        """
        Sets the additive_tax_money of this V1Payment.
        The sum of all additive taxes associated with the payment.

        :param additive_tax_money: The additive_tax_money of this V1Payment.
        :type: V1Money
        """

        self._additive_tax_money = additive_tax_money

    @property
    def tax_money(self):
        """
        Gets the tax_money of this V1Payment.
        The total of all taxes applied to the payment. This is always the sum of inclusive_tax_money and additive_tax_money.

        :return: The tax_money of this V1Payment.
        :rtype: V1Money
        """
        return self._tax_money

    @tax_money.setter
    def tax_money(self, tax_money):
        """
        Sets the tax_money of this V1Payment.
        The total of all taxes applied to the payment. This is always the sum of inclusive_tax_money and additive_tax_money.

        :param tax_money: The tax_money of this V1Payment.
        :type: V1Money
        """

        self._tax_money = tax_money

    @property
    def tip_money(self):
        """
        Gets the tip_money of this V1Payment.
        The total of all tips applied to the payment.

        :return: The tip_money of this V1Payment.
        :rtype: V1Money
        """
        return self._tip_money

    @tip_money.setter
    def tip_money(self, tip_money):
        """
        Sets the tip_money of this V1Payment.
        The total of all tips applied to the payment.

        :param tip_money: The tip_money of this V1Payment.
        :type: V1Money
        """

        self._tip_money = tip_money

    @property
    def discount_money(self):
        """
        Gets the discount_money of this V1Payment.
        The total of all discounts applied to the payment.

        :return: The discount_money of this V1Payment.
        :rtype: V1Money
        """
        return self._discount_money

    @discount_money.setter
    def discount_money(self, discount_money):
        """
        Sets the discount_money of this V1Payment.
        The total of all discounts applied to the payment.

        :param discount_money: The discount_money of this V1Payment.
        :type: V1Money
        """

        self._discount_money = discount_money

    @property
    def total_collected_money(self):
        """
        Gets the total_collected_money of this V1Payment.
        The total of all discounts applied to the payment.

        :return: The total_collected_money of this V1Payment.
        :rtype: V1Money
        """
        return self._total_collected_money

    @total_collected_money.setter
    def total_collected_money(self, total_collected_money):
        """
        Sets the total_collected_money of this V1Payment.
        The total of all discounts applied to the payment.

        :param total_collected_money: The total_collected_money of this V1Payment.
        :type: V1Money
        """

        self._total_collected_money = total_collected_money

    @property
    def processing_fee_money(self):
        """
        Gets the processing_fee_money of this V1Payment.
        The total of all processing fees collected by Square for the payment.

        :return: The processing_fee_money of this V1Payment.
        :rtype: V1Money
        """
        return self._processing_fee_money

    @processing_fee_money.setter
    def processing_fee_money(self, processing_fee_money):
        """
        Sets the processing_fee_money of this V1Payment.
        The total of all processing fees collected by Square for the payment.

        :param processing_fee_money: The processing_fee_money of this V1Payment.
        :type: V1Money
        """

        self._processing_fee_money = processing_fee_money

    @property
    def net_total_money(self):
        """
        Gets the net_total_money of this V1Payment.
        The amount to be deposited into the merchant's bank account for the payment.

        :return: The net_total_money of this V1Payment.
        :rtype: V1Money
        """
        return self._net_total_money

    @net_total_money.setter
    def net_total_money(self, net_total_money):
        """
        Sets the net_total_money of this V1Payment.
        The amount to be deposited into the merchant's bank account for the payment.

        :param net_total_money: The net_total_money of this V1Payment.
        :type: V1Money
        """

        self._net_total_money = net_total_money

    @property
    def refunded_money(self):
        """
        Gets the refunded_money of this V1Payment.
        The total of all refunds applied to the payment.

        :return: The refunded_money of this V1Payment.
        :rtype: V1Money
        """
        return self._refunded_money

    @refunded_money.setter
    def refunded_money(self, refunded_money):
        """
        Sets the refunded_money of this V1Payment.
        The total of all refunds applied to the payment.

        :param refunded_money: The refunded_money of this V1Payment.
        :type: V1Money
        """

        self._refunded_money = refunded_money

    @property
    def swedish_rounding_money(self):
        """
        Gets the swedish_rounding_money of this V1Payment.


        :return: The swedish_rounding_money of this V1Payment.
        :rtype: V1Money
        """
        return self._swedish_rounding_money

    @swedish_rounding_money.setter
    def swedish_rounding_money(self, swedish_rounding_money):
        """
        Sets the swedish_rounding_money of this V1Payment.


        :param swedish_rounding_money: The swedish_rounding_money of this V1Payment.
        :type: V1Money
        """

        self._swedish_rounding_money = swedish_rounding_money

    @property
    def gross_sales_money(self):
        """
        Gets the gross_sales_money of this V1Payment.


        :return: The gross_sales_money of this V1Payment.
        :rtype: V1Money
        """
        return self._gross_sales_money

    @gross_sales_money.setter
    def gross_sales_money(self, gross_sales_money):
        """
        Sets the gross_sales_money of this V1Payment.


        :param gross_sales_money: The gross_sales_money of this V1Payment.
        :type: V1Money
        """

        self._gross_sales_money = gross_sales_money

    @property
    def net_sales_money(self):
        """
        Gets the net_sales_money of this V1Payment.


        :return: The net_sales_money of this V1Payment.
        :rtype: V1Money
        """
        return self._net_sales_money

    @net_sales_money.setter
    def net_sales_money(self, net_sales_money):
        """
        Sets the net_sales_money of this V1Payment.


        :param net_sales_money: The net_sales_money of this V1Payment.
        :type: V1Money
        """

        self._net_sales_money = net_sales_money

    @property
    def inclusive_tax(self):
        """
        Gets the inclusive_tax of this V1Payment.
        All of the inclusive taxes associated with the payment.

        :return: The inclusive_tax of this V1Payment.
        :rtype: list[V1PaymentTax]
        """
        return self._inclusive_tax

    @inclusive_tax.setter
    def inclusive_tax(self, inclusive_tax):
        """
        Sets the inclusive_tax of this V1Payment.
        All of the inclusive taxes associated with the payment.

        :param inclusive_tax: The inclusive_tax of this V1Payment.
        :type: list[V1PaymentTax]
        """

        self._inclusive_tax = inclusive_tax

    @property
    def additive_tax(self):
        """
        Gets the additive_tax of this V1Payment.
        All of the additive taxes associated with the payment.

        :return: The additive_tax of this V1Payment.
        :rtype: list[V1PaymentTax]
        """
        return self._additive_tax

    @additive_tax.setter
    def additive_tax(self, additive_tax):
        """
        Sets the additive_tax of this V1Payment.
        All of the additive taxes associated with the payment.

        :param additive_tax: The additive_tax of this V1Payment.
        :type: list[V1PaymentTax]
        """

        self._additive_tax = additive_tax

    @property
    def tender(self):
        """
        Gets the tender of this V1Payment.
        All of the additive taxes associated with the payment.

        :return: The tender of this V1Payment.
        :rtype: list[V1Tender]
        """
        return self._tender

    @tender.setter
    def tender(self, tender):
        """
        Sets the tender of this V1Payment.
        All of the additive taxes associated with the payment.

        :param tender: The tender of this V1Payment.
        :type: list[V1Tender]
        """

        self._tender = tender

    @property
    def refunds(self):
        """
        Gets the refunds of this V1Payment.
        All of the refunds applied to the payment.

        :return: The refunds of this V1Payment.
        :rtype: list[V1Refund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """
        Sets the refunds of this V1Payment.
        All of the refunds applied to the payment.

        :param refunds: The refunds of this V1Payment.
        :type: list[V1Refund]
        """

        self._refunds = refunds

    @property
    def itemizations(self):
        """
        Gets the itemizations of this V1Payment.
        The items purchased in the payment.

        :return: The itemizations of this V1Payment.
        :rtype: list[V1PaymentItemization]
        """
        return self._itemizations

    @itemizations.setter
    def itemizations(self, itemizations):
        """
        Sets the itemizations of this V1Payment.
        The items purchased in the payment.

        :param itemizations: The itemizations of this V1Payment.
        :type: list[V1PaymentItemization]
        """

        self._itemizations = itemizations

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
