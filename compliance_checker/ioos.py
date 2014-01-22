import json
import itertools
from compliance_checker.base import BaseCheck, BaseNCCheck, BaseSOSCheck, check_has, score_group, Result
from pkgutil import get_data

class IOOSBaseCheck(BaseCheck):

    ###############################################################################
    #
    # HIGHLY RECOMMENDED
    # 
    ###############################################################################

    @check_has(BaseCheck.HIGH)
    def check_high(self, ds):
        return [
            'operator_email',
            'operator_name',
            'platform_sponsor',
            'platform_type',
            'publisher',
            'publisher_email',
            'station_id',
            'station_long_name',
            'station_name',
            'station_short_name',
            'station_wmo_id',
            'time_period_begin',
            'time_period_end',
            'time_period_interval',
            'time_period_interval_units',
                        ]

    ###############################################################################
    #
    # RECOMMENDED
    #
    ###############################################################################

    @check_has(BaseCheck.MEDIUM)
    def check_recommended(self, ds):
        return [
            'location_units',
            'observed_property',
            'observed_property_time_last',
            'operator_address',
            'operator_sector',
            'sensor_descriptions',
            'sensor_ids',
            'sensor_names',
            'service_contact_address',
            'service_contact_email',
            'service_contact_name',
            'service_keyword_1',
            'service_provider_name',
            'service_title',
            'service_type_name',
            'service_type_version',
            'sos_template_version',
            'station_deployment_end',
            'station_deployment_start',
            'variable_altitudes',
            'variable_names',
            'variable_units'
        ]

    ###############################################################################
    #
    # SUGGESTED
    #
    ###############################################################################

    @check_has(BaseCheck.LOW)
    def check_suggested(self, ds):
        return [
            'altitude_units'
                ]

class IOOSNCCheck(BaseNCCheck, IOOSBaseCheck):
    # belefs
    @classmethod
    def beliefs(cls):
        f = get_data("compliance_checker", "data/ioos-metamap-ncml.json")
        beliefs = json.loads(f)

        # strip out metadata
        return {k:v for k,v in beliefs.iteritems() if not k.startswith("__")}

class IOOSSOSCheck(BaseSOSCheck, IOOSBaseCheck):
    # beliefs
    @classmethod
    def beliefs(cls):
        f = get_data("compliance_checker", "data/ioos-metamap-sos-gc.json")
        beliefs = json.loads(f)

        # strip out metadata
        return {k:v for k,v in beliefs.iteritems() if not k.startswith("__")}


