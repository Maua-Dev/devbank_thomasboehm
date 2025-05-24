from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments
from .entities.user import User
from .errors.entity_errors import ParamNotValidated

app = FastAPI()

user_repo = Environments.get_user_repo()()
transaction_repo = Environments.get_transaction_repo()(user_repo)

in_use_user_id = 1
factor = 2
user = User(name={"Vitor Soller"}, agency={'0000'}, account={'00000-0'}, current_balance={1000.0})
user_repo.create_user(user)
@app.get("/")
def get_user(in_use_user_id: int = in_use_user_id):
    user = user_repo.get_user(user_id=in_use_user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user.to_dict()

@app.get("/history")
def get_history():
    history = transaction_repo.get_transactions()
    if history is None:
        return None
    else:
        return transaction_repo.all_transactions


@app.post("/deposit", status_code=201)
def deposit(request: dict):
    model = {
        "2":0,
        "5":0,
        "10":0,
        "20":0,
        "50":0,
        "100":0,
        "200":0
    }
    
    transaction_value = 0.0
    
    for key in request:
        if model.get(key, None) is not None:
            transaction_value += int(key) * float(request[key])

    user = user_repo.get_user(user_id=in_use_user_id)

    if transaction_value >= user.current_balance * factor:
        raise HTTPException(status_code=403, detail="Depósito Suspeito")
    response = transaction_repo.update_current_balance(user_id=in_use_user_id, transaction_type="DEPOSIT", value=transaction_value)
    return response

@app.post("/withdraw", status_code=201)
def withdraw(request: dict):
    model = {
        "2":0,
        "5":0,
        "10":0,
        "20":0,
        "50":0,
        "100":0,
        "200":0
    }
    
    transaction_value = 0.0
    
    for key in request:
        if model.get(key, None) is not None:
            transaction_value += int(key) * float(request[key])

    user = user_repo.get_user(user_id=in_use_user_id)

    if transaction_value > user.current_balance:
        raise HTTPException(status_code=403, detail="Saldo insuficiente para transação")
    response = transaction_repo.update_current_balance(user_id=in_use_user_id, transaction_type="WITHDRAW", value=transaction_value)
    return response

handler = Mangum(app, lifespan="off")


@app.post("/users/create_user", status_code=201)
def create_user(request: dict):
    user_id = request.get("user_id")

    validation_user_id = user_repo.validate_user_id(user_id=user_id)
    if not validation_user_id[0]:
        raise HTTPException(status_code=400, detail=validation_user_id[1])
    user = user_repo.get_user(user_id=user_id)

    validation_name = user_repo.validate_name(name=name)
    if not validation_name[0]:
        raise HTTPException(status_code=400, detail=validation_name[1])
    name = request.get("name")

    validation_agency = user_repo.validate_agency(agency=agency)
    if not validation_agency[0]:
        raise HTTPException(status_code=400, detail=validation_agency[1])
    agency = request.get("agency")

    validation_account_number = user_repo.validate_account_number(account_number=account_number)
    if not validation_account_number[0]:
        raise HTTPException(status_code=400, detail=validation_account_number[1])
    account_number = request.get("account_number")

    validation_current_balance = user_repo.validate_current_balance(current_balance=current_balance)
    if not validation_current_balance[0]:
        raise HTTPException(status_code=400, detail=validation_current_balance[1])
    current_balance = request.get("current_balance")

    try:
        user = User(name=name, agency=agency, account_number=account_number, current_balance=current_balance)
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)
    
    user_response = user_repo.create_item(user, user_id)
    return {
        "user_id": user_id,
        "user": user_response.to_dict()
    }