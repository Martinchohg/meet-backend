from database import db, create_app
from werkzeug.exceptions import HTTPException
# from views import
from flask import jsonify
# from utils.email_utils import setup_mail_sender
# from populators.notification_initializer import NotificationInitializer
# from populators.role_initializer import RoleInitializer
# from populators.company_initializer import CompanyInitializer
# from populators.education_level_initializer import EducationLevelInitializer
# from populators.extra_fields_initializer import EventResponseInitializer, MaritalStatusInitializer
# from populators.notification_type_initializer import NotificationTypeInitializer
# from populators.recognition_type_initializer import RecognitionTypeInitializer
# from populators.time_off_initializer import TimeOffInitializer
# from populators.relationships_initializer import RelationshipInitializer
# from populators.suggestion_resolutions_initializer import SuggestionResolutionInitializer
# from populators.user_status_initializer import UserStatusInitializer
import os

API_PREFIX = "/api/v1"

application = create_app()


# setup_mail_sender(application)


@application.errorhandler(401)
@application.errorhandler(404)
@application.errorhandler(403)
@application.errorhandler(412)
@application.errorhandler(400)
@application.errorhandler(500)
def handle_error(e):
    code = 500
    message = None
    if isinstance(e, HTTPException):
        code = e.code
        message = e.description
        error = str(e)
    else:
        message = e.message
        error = "500: Internal Server Error"
    return jsonify(error=error, message=message), code


@application.teardown_appcontext
def shutdown_session(response_or_exc):
    try:
        if response_or_exc is None:
            db.session.commit()
    finally:
        db.session.remove()
    return response_or_exc


@application.route("/ping")
def hello():
    return jsonify(message="Pong!"), 200


# CityView.register(application, route_prefix=API_PREFIX)


if __name__ == '__main__':
    with application.app_context():
        db.create_all()
        # NotificationInitializer().init_notification_types()
        # RoleInitializer().init_permissions()
        # RoleInitializer().init_roles()
        # CompanyInitializer().init_companies()
        # EducationLevelInitializer().init_education_levels()
        # EventResponseInitializer().init_event_responses()
        # MaritalStatusInitializer().init_marital_statues()
        # NotificationTypeInitializer().init_notification_types()
        # RecognitionTypeInitializer().init_recognition_type()
        # time_off_initilizers = TimeOffInitializer()
        # time_off_initilizers.init_time_off_statuses()
        # time_off_initilizers.init_time_off_types()
        # RelationshipInitializer().init_relationships()
        # SuggestionResolutionInitializer().init_suggestion_resolutions()
        # UserStatusInitializer().init_user_statuses()
        application.run(host=os.getenv("APP_HOST", "0.0.0.0"), port=os.getenv("PORT", 5000))
