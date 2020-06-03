from main import create_token, verify_signature


class TestChallenge4:
    token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'

    def test_create_token(self):
        assert create_token({"language": "Python"}, "acelera") == self.token

    def test_verify_signature(self):
        assert verify_signature(self.token) == {"language": "Python"}

    def test_verify_signature_with_error(self):
        assert verify_signature('testestest') == {"error": 2}