from .activity_descriptor import get_analytics_contract

SAMPLE_STUDENT_IDS = ["1001", "1002"]
SAMPLE_VALUES = {"boolean": True, "integer": 1, "text/plain": "sample"}


def _sample_value(analytic, activity_id, student_id, base_url):
    # Gera um valor de exemplo
    if analytic["type"] == "URL":
        return f"{base_url}report/{activity_id}/{student_id}/{analytic['name']}"
    return SAMPLE_VALUES.get(analytic["type"])


def _with_values(analytics, activity_id, student_id, base_url):
    # Acrescenta o campo "value" a cada analytic
    return [
        {**analytic, "value": _sample_value(analytic, activity_id, student_id, base_url)}
        for analytic in analytics
    ]


def get_instance_analytics(activity_id, base_url):
    # Devolve as analytics-exemplo para os alunos da instância
    contract = get_analytics_contract()
    return [
        {
            "inveniraStdID": student_id,
            "quantAnalytics": _with_values(
                contract["quantAnalytics"], activity_id, student_id, base_url
            ),
            "qualAnalytics": _with_values(
                contract["qualAnalytics"], activity_id, student_id, base_url
            ),
        }
        for student_id in SAMPLE_STUDENT_IDS
    ]