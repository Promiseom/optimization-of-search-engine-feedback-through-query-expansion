from flask import Flask, jsonify
from flask_restful import request, Api
import qe_model
from term_selector import TermSelector

application = Flask(__name__)
api = Api(application)

@application.route("/")
def home():
    return "This server hosts a query expansion model developed by Promise Anendah for his undergraduate project with and API what will be used to access it."

@application.route("/expand", methods=['GET'])
def expandQuery():
    response = {"status_code": 400, "message": None}
    if("query" in request.args):
        user_query = request.args['query']
        response['status_code'] = 200
        result = qe_model.get_candidate_expansion_terms(user_query)

        # refine the expanded terms
        if result is not None:
            cand_expansion_terms = result['raw_expansion_terms']
            ts = TermSelector()
            cats = ts.refine_terms(cand_expansion_terms, result['query'])

            ex_terms = "";
            for i in cats[1][:5]:
                ex_terms += i + ' '
            ex_terms.strip()
            expanded_query = result['query'] + ' ' + ex_terms
            response["message"] = expanded_query
            response["expanded"] = True
        else:
            response["message"] = user_query
            response["expanded"] = False
    else:
        response["message"] = "Invalid query value, no query value has been supplied."
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    application.run()
