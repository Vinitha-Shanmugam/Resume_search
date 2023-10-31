import requests
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from Resume_app import serializers
import logging

_logger = logging.getLogger(__name__)


def search_profiles(access_token, search_params):
    try:
        url = 'https://talent-api.dice.com/v2/profiles/search'
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers, params=search_params)
        return response

    except Exception as e:
        print("An error occurred:", str(e))
        return None


class JobBoardResumeSearch(GenericAPIView):
    serializer_class = serializers.ResumeSearchSerializer

    def post(self, request, **kwargs):
        try:
            search_query = "python"
            user_name = "mrashed@vrdella.com"
            access_token = "e7cbfd0e-d080-5677-8677-06bec6967879"  # Replace with your Dice.com access token
            search_params = {
                'locations': '[{"value":"Toronto,Canada"}]',
                'skillsKeyword': 'python AND data analysis',
                'skillYearsOfExperience': '["python|18","data analysis|3"]',
                'skills': ['python,software,data analysis,opentext'],
                'jobTitleKeyword': 'Technical Architect',
                'jobTitle': 'QRP',
                'companyKeyword': 'good',
                'companyCurrent': 'false',
                'company': 'good',
                'lastActive': 120,
                'searchType': 'Integrated',
                'excludeThirdParty': 'false',
                'willingToRelocate': 'false',
                'hasEmail': 'true',
                'hasPhoneNumber': 'true',
                'likelyToSwitch': 'false',
                'likelyToMove': '{"max":0}',
                'yearsExperience': '{"min": 1, "max":30 }',
                'educationDegree': '',
                'language':'python',
                # 'language': 'Italian or Spanish AND english or Spanish OR English',
                'socialProfiles': ['Dice','facebook','linkedin','twitter'],
                'excludeFounders': 'false',
                'hasPatent': 'false',
                'dateResumeLastUpdated': 300,
                'employmentType': 'full-time,part-time',
                'workPermitLocation': 'US',
                'workPermit': "TN Permit Holder",
                'compensation': '{"min":75,"max":0,"currency":"USD","frequency":"hourly","includeUnspecified": false}',
                'onlyWithSecurityClearance': 'true',
                'willingToRelocatePreferredLocationsOnly': 'false',
                'willingToRelocateIncludeLocals': 'false',
                'travelPreference': '0',
                'facets': 'company, skills, jobTitle',
                'sortBy': 'relevancy',
                'sortByDirection': 'asc',
                'page': '1',
                'pageSize': '25'
            }

            job_search_response = search_profiles(access_token, search_params)
            query = str(job_search_response)
            job_search_response_details = job_search_response.json()
            if query == "<Response [200]>":
                data = {
                    'response_code': 200,
                    'message': 'Resume search is fetched successfully.',
                    'statusFlag': True,
                    'status': 'SUCCESS',
                    'errorDetails': None,
                    'data': job_search_response_details
                }
                _logger.info("Resume search is fetched successfully.")
                return Response(data)

        except Exception as e:
            data = {
                'response_code': 500,
                'message': 'Resume search fetching was failed.',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': {"trace": str(e)},
                'data': {}
            }
            _logger.error("Resume search fetching was failed.")
            return Response(data)

#
# class ResumeSearchSerializer(serializers.Serializer):
#     search_query = serializers.CharField()
#     user_name = serializers.CharField()
