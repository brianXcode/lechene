from flask import Response, jsonify, request
from flask_restful import Resource
from scr.database.models import Measurement
from scr.utility.errors import FieldDoesNotExistError, SchemaValidationError
from mongoengine.errors import ValidationError



class MeasurementApi(Resource):
    def get(self):
        measurement = Measurement.objects.all()
        return Response(measurement.to_json(), mimetype="applicaton/json", status=200)

    def post(self):
        try:
            data = request.get_json()
            measurement = Measurement.objects.create(
                custom_order_id = data["custom_order_id"],
                gender = data["gender"],
                shoulder = data["shoulder"],
                hand_length = data["hand_length"],
                chest_bust = data["chest_bust"],
                stomach = data["stomach"],
                top_lenght = data["top_lenght"],
                round_arm = data["round_arm"],
                waist = data["waist"],
                tigh = data["tigh"],
                knee = data["knee"],
                around_leg = data["around_leg"],
                leg_length = data["leg_length"],
                sizes = data["sizes"],
                other_info = data["other_info"]
            )

            measurement.save()
            return Response(measurement.to_json(), mimetype="application/json", status=200)
        except (FieldDoesNotExistError, ValidationError):
            raise SchemaValidationError


class MeasurementDetailsApi(Resource):
    def get(self, id):
        try:
            measurement = Measurement.objects.get(id=id)
            return Response(measurement.to_json(), mimetype="applicaton/json", status=200)
        except:
             return jsonify( 
                message="that Id does not exist",
                status=404
            )

    def put(self, id):
        try:

            measurement = Measurement.objects.get(id=id)
            data = request.get_json()

            measurement.update(
                custom_order_id = data["custom_order_id"],
                gender = data["gender"],
                shoulder = data["shoulder"],
                hand_length = data["hand_length"],
                chest_bust = data["chest_bust"],
                stomach = data["stomach"],
                top_lenght = data["top_lenght"],
                round_arm = data["round_arm"],
                waist = data["waist"],
                tigh = data["tigh"],
                knee = data["knee"],
                around_leg = data["around_leg"],
                leg_length = data["leg_length"],
                sizes = data["sizes"],
                other_info = data["other_info"]
            )

            measurement.save()
            return Response(measurement.to_json(), mimetype="application/json", status=200)
        except :
            return jsonify(
                message="that Id does not exist or check the payload",
                status=404
            )

  
    
    def delete(self, id):
        try:
            update_measurement = Measurement.objects.get(id=id)
            update_measurement.delete()
            return jsonify({
                "message": "Delivery deleted successfully"
            })
        except Exception:
            return jsonify(
                message="that Id does not exist",
                status=404
            )




class MeasurementSearchApi(Resource):
    def get(self):
     
        custom_order_id = request.args.get("custom_order_id")
        gender = request.args.get("gender")
        shoulder = request.args.get("shoulder")
        hand_length = request.args.get("hand_length")
        chest_bust =request.args.get("chest_bust")
        stomach = request.args.get("stomach")
        top_lenght = request.args.get("top_lenght")
        round_arm = request.args.get("round_arm")
        waist = request.args.get("waist")
        tigh = request.args.get("tigh")
        knee = request.args.get("knee")
        around_leg = request.args.get("around_leg")
        leg_length = request.args.get("leg_length")
        sizes = request.args.get("sizes")
        other_info = request.args.get("other_info")
        created_at = request.args.get("created_at")

        if custom_order_id:
            measurement= Measurement.objects(custom_order_id__icontains = custom_order_id)
        elif gender:
            measurement = Measurement.objects(gender__icontains = gender)
        elif shoulder:
            measurement = Measurement.objects(shoulder__icontains = shoulder)
        elif hand_length:
            measurement = Measurement.objects(hand_length__icontains = hand_length)
        elif chest_bust:
           measurement =  Measurement.objects(chest_bust__icontains = chest_bust)
        elif  stomach:
           measurement =  Measurement.objects( stomach__icontains =  stomach)
        elif top_lenght:
           measurement=  Measurement.objects(top_lenght__icontains = top_lenght)
        elif round_arm:
           measurement=  Measurement.objects(round_arm__icontains = round_arm)
        elif waist:
           measurement =  Measurement.objects(waist__icontains = waist)
        elif tigh:
           measurement =  Measurement.objects(tigh__icontains = tigh)
        elif knee:
           measurement =  Measurement.objects(knee__icontains = knee)
        elif knee:
           measurement =  Measurement.objects(knee__icontains = knee)
        elif around_leg:
           measurement =  Measurement.objects(around_leg__icontains = around_leg)
        elif leg_length:
           measurement =  Measurement.objects(leg_length__icontains = leg_length)
        elif sizes:
           measurement =  Measurement.objects(sizes__icontains = sizes)
        elif other_info:
           measurement =  Measurement.objects(other_info__icontains = other_info)
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })   
        return Response( measurement.to_json(), mimetype="application/json", status=200 )


