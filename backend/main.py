from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, User as UserModel  # 从 models 导入并使用别名
from schemas import UserCreate, User, UserLogin  # 从 schemas 导入 Pydantic 模型
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#CORS 错误
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite 默认端口
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 创建数据库表
Base.metadata.create_all(bind=engine)

# register
@app.post("/account/register/", response_model=User)
async def userRegister(user: UserCreate, db: Session = Depends(get_db)):
    # 使用 models.UserModel 而不是 schemas.User
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # 创建新用户
    new_user = UserModel(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# login
@app.post("/account/login/", response_model=User)
async def user_login(login_data: UserLogin, db: Session = Depends(get_db)):
    # 查询用户
    user = db.query(UserModel).filter(UserModel.username == login_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # 验证密码
    if user.password != login_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # 返回用户信息
    return user

