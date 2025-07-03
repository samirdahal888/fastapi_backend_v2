from sqlmodel import Field, SQLModel


class AdminBase(SQLModel):
    username: str = Field(index=True)


class Admin(AdminBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str


class AdminPublic(AdminBase):
    id: int


class AdminCreate(AdminBase):
    password: str


class AdminUpdate(AdminBase):
    username: str | None = None
    password: str | None = None


class StudentBase(SQLModel):
    name: str
    age: int
    rollno: int


class Student(StudentBase, table=True):
    id: int = Field(default=None, primary_key=True)
    password: str


class StudentPublic(AdminBase):
    id: int


class StudenCreate(StudentBase):
    password: str


class StudentUpdate(StudentBase):
    username: str | None = None
    password: str | None = None
