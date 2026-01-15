
# logique de validation

from loader import load_env_secure
from schema import load_schema


def display(report):
    print("=================================")
    print("Report on environmental variables")
    print("=================================")
    print("\n")

    for _, txt in enumerate(report):
        print(f"{txt}")
    
    print("\n")
    print("=================================")
    print("\n")



def validate(untreated_env, schema):

    report = []

    for key in list(schema.keys()) : 
        if key not in list(untreated_env.keys()):
            if schema[key]['required'] == True:
                report.append(f"❌ {key} is missing")
            else :
                report.append(f"⚠️  {key} is missing")
        else : 
            if untreated_env[key] == "" :
                report.append(f"❌ {key} value missing")
            else :
                if schema[key]['type'] == "int" : # verifier si c'est un int
                    try:
                        _ = int(untreated_env[key]) # vu que on a que des str on tente de le passer en int si ca marche c'est que c'est des chiffre (int) sinon un string
                    except (FileNotFoundError, ValueError, PermissionError) as e:
                        report.append(f"❌ {key} should be int")

                elif schema[key]['type'] == "bool" : # verifier si c'est un booleen 
                    if untreated_env[key] == "False" or untreated_env[key] == "True" or untreated_env[key] == "FALSE" or untreated_env[key] == "TRUE" :
                        report.append(f"⚠️  {key} should be lowercase boolean")
                    elif untreated_env[key] != "false" and untreated_env[key] != "true":
                        report.append(f"❌ {key} should be bool")

                elif schema[key]['type'] == "string" : # Meme stratégie que pour les int mais si il est rentré dans le except alors c'est good
                    is_int = True
                    try:
                        _ = int(untreated_env[key])
                    except (FileNotFoundError, ValueError, PermissionError) as e:
                        is_int = False
                    if is_int == True :
                        report.append(f"❌ {key} should be string")


    for key in list(untreated_env.keys()) :
        if key not in list(schema.keys()):
            report.append(f"❌ {key} unknown variable")
    

    return report



def cli_validate(env_path, schema_path):
    untreated_env, masked_env = load_env_secure(env_path)

    schema = load_schema(schema_path)

    report = validate(untreated_env=untreated_env, schema=schema)

    display(report)



def test_cli_validate():
    env_path =  "./examples/.env"
    schema_path = "./examples/env_schema.yml"

    cli_validate(env_path=env_path, schema_path=schema_path)


test_cli_validate()