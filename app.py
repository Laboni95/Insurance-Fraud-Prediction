from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("insurance_model.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        Months_as_Customer = int(request.form["months_as_customer"])
        Policy_Deductable = int(request.form["policy_deductable"])
        Umbrella_limit = int(request.form["umbrella_limit"])

        Capital_Gains = int(request.form["capital_gains"])
        Capital_Loss = int(request.form["capital_loss"])
        Incident_Hour_of_the_Day = int(request.form["incident_hour_of_the_day"])
        Number_of_Vehicles_Involved = int(request.form["numbers_of_vehicles_involved"])
        Bodily_Injuries = int(request.form["bodyly_injuries"])
        Witnesses = int(request.form["witnesses"])
        Injury_Claim = int(request.form["injury_claim"])
        Property_Claim = int(request.form["property_claim"])
        Vehicle_Claim = int(request.form["vehicle_claim"])
        Policy_annual_Premium = int(request.form["policy_annual_premium"])

        policy_csl = request.form['policy_csl']
        if (policy_csl == 'policy_csl_250'):
            policy_csl_250 = 1
            policy_csl_500 = 0
        elif(policy_csl == 'policy_csl_500'):
            policy_csl_250 = 0
            policy_csl_500 = 1
        else:
            policy_csl_250 = 0
            policy_csl_500 = 0

        insured_education_level = request.form['insured_education_level']
        if (insured_education_level == 'insured_education_level_College'):
            insured_education_level_College = 1
            insured_education_level_HighSchool = 0
            insured_education_level_JD = 0
            insured_education_level_MD = 0
            insured_education_level_Masters = 0
            insured_education_level_PhD = 0
        elif (insured_education_level == 'insured_education_level_HighSchool'):
            insured_education_level_College = 0
            insured_education_level_HighSchool = 1
            insured_education_level_JD = 0
            insured_education_level_MD = 0
            insured_education_level_Masters = 0
            insured_education_level_PhD = 0
        elif (insured_education_level == 'insured_education_level_JD'):
            insured_education_level_College = 0
            insured_education_level_HighSchool = 0
            insured_education_level_JD = 1
            insured_education_level_MD = 0
            insured_education_level_Masters = 0
            insured_education_level_PhD = 0
        elif (insured_education_level == 'insured_education_level_MD'):
            insured_education_level_College = 0
            insured_education_level_HighSchool = 0
            insured_education_level_JD = 0
            insured_education_level_MD = 1
            insured_education_level_Masters = 0
            insured_education_level_PhD = 0
        elif (insured_education_level == 'insured_education_level_Masters'):
            insured_education_level_College = 0
            insured_education_level_HighSchool = 0
            insured_education_level_JD = 0
            insured_education_level_MD = 0
            insured_education_level_Masters = 1
            insured_education_level_PhD = 0
        elif (insured_education_level == 'insured_education_level_PhD'):
            insured_education_level_College = 0
            insured_education_level_HighSchool = 0
            insured_education_level_JD = 0
            insured_education_level_MD = 0
            insured_education_level_Masters = 0
            insured_education_level_PhD = 1
        else:
            insured_education_level_College = 0
            insured_education_level_HighSchool = 0
            insured_education_level_JD = 0
            insured_education_level_MD = 0
            insured_education_level_Masters = 0
            insured_education_level_PhD = 0

        insured_sex = request.form['insured_sex']
        if (insured_sex == "insured_sex_MALE"):
            insured_sex_MALE = 1
        else:
            insured_sex_MALE = 0

        insured_occupation = request.form['insured_occupation']
        if (insured_occupation == 'insured_occupation_armed-forces'):
            insured_occupation_armed_forces = 1
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_craft_repair'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 1
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv =0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_exec - managerial'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 1
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_farming_fishing'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 1
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0

        elif (insured_occupation == 'insured_occupation_handlers_cleaners'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial =0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 1
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_machine_op_inspct'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 1
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_other_service'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 1
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_priv - house - serv'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 1
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_prof_specialty'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 1
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_protective_serv'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 1
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_sales'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 1
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_tech_support'):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 1
            insured_occupation_transport_moving = 0
        elif (insured_occupation == 'insured_occupation_transport_moving' ):
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 1

        else:
            insured_occupation_armed_forces = 0
            insured_occupation_craft_repair = 0
            insured_occupation_exec_managerial = 0
            insured_occupation_farming_fishing = 0
            insured_occupation_handlers_cleaners = 0
            insured_occupation_machine_op_inspct = 0
            insured_occupation_other_service = 0
            insured_occupation_priv_house_serv = 0
            insured_occupation_prof_specialty = 0
            insured_occupation_protective_serv = 0
            insured_occupation_sales = 0
            insured_occupation_tech_support = 0
            insured_occupation_transport_moving = 0

        insured_relationship = request.form['insured_relationship']
        if (insured_relationship == 'insured_relationship_not_in_family'):
            insured_relationship_not_in_family = 1
            insured_relationship_other_relative = 0
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 0
            insured_relationship_wife = 0
        elif (insured_relationship == 'insured_relationship_other_relative'):
            insured_relationship_not_in_family = 0
            insured_relationship_other_relative = 1
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 0
            insured_relationship_wife = 0
        elif (insured_relationship == 'insured_relationship_own_child'):
            insured_relationship_not_in_family = 0
            insured_relationship_other_relative = 0
            insured_relationship_own_child = 1
            insured_relationship_unmarried = 0
            insured_relationship_wife = 0
        elif (insured_relationship == 'insured_relationship_unmarried'):
            insured_relationship_not_in_family = 0
            insured_relationship_other_relative = 0
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 1
            insured_relationship_wife = 0
        elif (insured_relationship == 'insured_relationship_wife'):
            insured_relationship_not_in_family = 0
            insured_relationship_other_relative = 0
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 0
            insured_relationship_wife = 1
        else:
            insured_relationship_not_in_family = 0
            insured_relationship_other_relative = 0
            insured_relationship_own_child = 0
            insured_relationship_unmarried = 0
            insured_relationship_wife = 0

        incident_type = request.form['incident_type']
        if (incident_type == 'incident_type_ParkedCar'):
            incident_type_ParkedCar = 1
            incident_type_SingleVehicleCollision = 0
            incident_type_VehicleTheft = 0
        elif (incident_type == 'incident_type_SingleVehicleCollision'):
            incident_type_ParkedCar = 0
            incident_type_SingleVehicleCollision = 1
            incident_type_VehicleTheft = 0
        elif (incident_type == 'incident_type_VehicleTheft'):
            incident_type_ParkedCar = 0
            incident_type_SingleVehicleCollision = 0
            incident_type_VehicleTheft = 1
        else:
            incident_type_ParkedCar = 0
            incident_type_SingleVehicleCollision = 0
            incident_type_VehicleTheft = 0

        incident_severity = request.form['incident_severity']
        if (incident_severity == 'incident_severity_MinorDamage'):
            incident_severity_MinorDamage = 1
            incident_severity_TotalLoss = 0
            incident_severity_TrivialDamage = 0
        elif (incident_severity == 'incident_severity_TotalLoss'):
            incident_severity_MinorDamage = 0
            incident_severity_TotalLoss = 1
            incident_severity_TrivialDamage = 0
        elif (incident_severity == 'incident_severity_TrivialDamage'):
            incident_severity_MinorDamage = 0
            incident_severity_TotalLoss = 0
            incident_severity_TrivialDamage = 1
        else:
            incident_severity_MinorDamage = 0
            incident_severity_TotalLoss = 0
            incident_severity_TrivialDamage = 0

        collision_type = request.form['collision_type']
        if (collision_type == 'collision_type_RearCollision'):
            collision_type_RearCollision = 1
            collision_type_SideCollision = 0
        elif (collision_type == 'collision_type_SideCollision'):
            collision_type_RearCollision = 0
            collision_type_SideCollision = 1
        else:
            collision_type_RearCollision = 0
            collision_type_SideCollision = 0

        authorities_contacted = request.form['authorities_contacted']
        if (authorities_contacted == 'authorities_contacted_Fire' ):
            authorities_contacted_Fire = 1
            authorities_contacted_None = 0
            authorities_contacted_Other = 0
            authorities_contacted_Police = 0
        elif (authorities_contacted == 'authorities_contacted_None'):
            authorities_contacted_Fire = 0
            authorities_contacted_None = 1
            authorities_contacted_Other = 0
            authorities_contacted_Police = 0
        elif (authorities_contacted == 'authorities_contacted_Other'):
            authorities_contacted_Fire = 0
            authorities_contacted_None = 0
            authorities_contacted_Other = 1
            authorities_contacted_Police = 0
        elif (authorities_contacted == 'authorities_contacted_Police'):
            authorities_contacted_Fire = 0
            authorities_contacted_None = 0
            authorities_contacted_Other = 0
            authorities_contacted_Police = 1
        else:
            authorities_contacted_Fire = 0
            authorities_contacted_None = 0
            authorities_contacted_Other = 0
            authorities_contacted_Police = 0

        property_damage = request.form['property_damage']
        if (property_damage == 'property_damage_YES'):
            property_damage_YES = 1
        else:
            property_damage_YES = 0

        police_report_available = request.form['police_report_available']
        if (police_report_available == 'police_report_available_YES'):
            police_report_available_YES = 1
        else:

            police_report_available_YES = 0

        prediction = model.predict([[Months_as_Customer,
                                     Policy_Deductable,
                                     Umbrella_limit,
                                     Capital_Gains,
                                     Capital_Loss,
                                     Incident_Hour_of_the_Day,
                                     Number_of_Vehicles_Involved,
                                     Bodily_Injuries,
                                     Witnesses,
                                     Injury_Claim,
                                     Property_Claim,
                                     Vehicle_Claim,
                                     Policy_annual_Premium,
                                     policy_csl_250 / 500,
                                     policy_csl_500 / 1000,
                                     insured_education_level_College,
                                     insured_education_level_HighSchool,
                                     insured_education_level_JD,
                                     insured_education_level_MD,
                                     insured_education_level_Masters,
                                     insured_education_level_PhD,
                                     insured_sex_MALE,
                                     insured_occupation_armed_forces,
                                     insured_occupation_craft_repair,
                                     insured_occupation_exec_managerial,
                                     insured_occupation_farming_fishing,
                                     insured_occupation_handlers_cleaners,
                                     insured_occupation_machine_op_inspct,
                                     insured_occupation_other_service,
                                     insured_occupation_priv_house_serv,
                                     insured_occupation_prof_specialty,
                                     insured_occupation_protective_serv,
                                     insured_occupation_sales,
                                     insured_occupation_tech_support,
                                     insured_occupation_transport_moving,
                                     insured_relationship_not_in_family,
                                     insured_relationship_other_relative,
                                     insured_relationship_own_child,
                                     insured_relationship_unmarried,
                                     insured_relationship_wife,
                                     incident_type_ParkedCar,
                                     incident_type_SingleVehicleCollision,
                                     incident_type_VehicleTheft,
                                     incident_severity_MinorDamage,
                                     incident_severity_TotalLoss,
                                     incident_severity_TrivialDamage,
                                     collision_type_RearCollision,
                                     collision_type_SideCollision,
                                     authorities_contacted_Fire,
                                     authorities_contacted_None,
                                     authorities_contacted_Other,
                                     authorities_contacted_Police,
                                     property_damage_YES,
                                     police_report_available_YES]])
        output = prediction[0]

        if output == 0:
            return render_template('home.html', prediction_text='Insurance Fraud : No')
        else:
            return render_template('home.html', prediction_text='Insurance Fraud : Yes')


if __name__ == '__main__':
    app.run(debug = True)





