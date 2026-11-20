from flask import Response, abort, jsonify, render_template, request

from . import invenra_api_bp
from .. import activity_descriptor, analytics_service, instance_manager


@invenra_api_bp.get("/config")
def config_page():
    # Bloco HTML com os campos de configuração
    params = activity_descriptor.get_config_params()
    return render_template("config.html", params=params)


@invenra_api_bp.get("/json-params")
def json_params():
    return jsonify(activity_descriptor.get_config_params())


@invenra_api_bp.get("/deploy")
def deploy():
    # Recebe o ID da instância e devolve o URL de acesso à atividade
    activity_id = request.args.get("activityID")
    if not activity_id:
        abort(400, "Missing activityID")
    activity_url = instance_manager.create_instance(activity_id, request.url_root)
    return Response(activity_url, mimetype="text/plain")


@invenra_api_bp.get("/analytics-list")
def analytics_list():
    return jsonify(activity_descriptor.get_analytics_contract())


@invenra_api_bp.post("/analytics")
def analytics():
    body = request.get_json(force=True, silent=True)
    if not isinstance(body, dict) or not body.get("activityID"):
        abort(400, "Expected JSON body with activityID")
    response = analytics_service.get_instance_analytics(body["activityID"], request.url_root)
    return jsonify(response)