import os

from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from sqlalchemy.orm import mapped_column, Session
from sqlalchemy import String, Integer, BigInteger, DECIMAL, ForeignKey
from sqlalchemy import create_engine, UniqueConstraint
from dotenv import load_dotenv

load_dotenv()

BD_USER = os.getenv('DB_USER')
BD_PASSWORD = os.getenv('DB_PASSWORD')
BD_ADDRESS = os.getenv('DB_ADDRESS')
BD_PORT = os.getenv('DB_PORT')
BD_NAME = os.getenv('DB_NAME')

MEDIA_DIRECTORY = os.getenv('MEDIA_FOLDER')

engine = create_engine(f'postgresql://{BD_USER}:{BD_PASSWORD}@{BD_ADDRESS}:{BD_PORT}/{BD_NAME}', echo=False)


class Base(DeclarativeBase):
    pass


class Users(Base):
    """База пользователей"""
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    telegram: Mapped[int] = mapped_column(BigInteger, unique=True)
    phone: Mapped[str] = mapped_column(String(30), nullable=True)

    carts: Mapped[int] = relationship('Carts', back_populates='user_cart')

    def __str__(self):
        return self.name


class Carts(Base):
    """Временная корзина покупателя, используется до кассы"""
    __tablename__ = 'carts'
    id: Mapped[int] = mapped_column(primary_key=True)
    total_price: Mapped[DECIMAL] = mapped_column(DECIMAL(12, 2), default=0)
    total_products: Mapped[int] = mapped_column(Integer, default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)

    user_cart: Mapped[Users] = relationship(back_populates='carts')
    final_id: Mapped[int] = relationship('FinalCarts', back_populates='user_cart')

    def __str__(self):
        return str(self.id)


class FinalCarts(Base):
    """Окончательная корзина пользователя, возле кассы"""
    __tablename__ = 'final_carts'
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(50))
    final_price: Mapped[DECIMAL] = mapped_column(DECIMAL(12, 2), default=0)
    quantity: Mapped[int]

    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'))
    user_cart: Mapped[Carts] = relationship(back_populates='final_id')

    __table_args__ = (UniqueConstraint('cart_id', 'product_name'),)

    def __str__(self):
        return str(self.id)


class Categories(Base):
    """Категории продуктов"""
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(String(20), unique=True)

    products: Mapped['Products'] = relationship(back_populates='product_category')

    def __str__(self):
        return self.category_name


class Products(Base):
    """Продукты"""
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(20), unique=True)
    description: Mapped[str]
    image: Mapped[str] = mapped_column(String(100))
    price: Mapped[DECIMAL] = mapped_column(DECIMAL(12, 2), nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    product_category: Mapped[Categories] = relationship(back_populates='products')


def main():
    Base.metadata.create_all(engine)

    categories = ('Лаваши', 'Донары', 'Хот-Доги', 'Десерты', 'Соусы', 'Напитки')

    products = (
        (5, "Соус тартар", 1500.00, "Со́ус тарта́р (Tartare sauce, «татарский соус») – холодный соус из майонеза и зеленого лука.", "images/08fef660d1a54a2fb899333c7571aeba_sous_3.jpg"),
        (6, "Мятный чай", 5000.00, "Чай, мята", "images/fccdf0a847db4ed69f486e71c393a6c6_water_1.jpg"),
        (3, "Хот-дог с помидорами", 18000.00, "Булочки для хот-догов, Кетчуп, Майонез, Горчица, Помидор, Сосиски", "images/d8f811e247d74365893b2ce29a6e74cf_hot-dog_2.jpg"),
        (1, "Мини Лаваш", 20000.00, "Лаваш", "images/14380b44ceec402584510c19ae9589af_lavash_1.jpg"),
        (1, "Мини Говяжий", 17000.00, "Лаваш, Говядина", "images/61c4df3ff4ee400090e60738f787276f_lavash_2.jpg"),
        (1, "Мини с сыром", 19500.00, "Лаваш, сыр, специи", "images/7ce6a9cee9a44043999c34451c713214_lavash_3.jpg"),
        (2, "Донар с курицей", 23000.00, "Мука пшеничная, вода, грудка куриная-гриль, соус Цезарь, огурцы свежие и маринованные, томаты, молоко сухое, закваска пшеничная (мука пшеничная 1С, мука ржаная, дрожжи, отруби пшеничные, клейковина пшеничная), лук красный, укроп, сахар, соль, томатная паста, прованские травы, дрожжи.", "images/195040c15cd2488385aa377ff3ecf2d5_donar_2.jpg"),
        (2, "Донар со свининой", 24000.00, "Мука пшеничная, вода, свинина маринованная, соус Цезарь, огурцы свежие и маринованные, томаты, молоко сухое, закваска пшеничная (мука пшеничная 1С, мука ржаная, дрожжи, отруби пшеничные, клейковина пшеничная), лук красный, укроп, сахар, томатная паста, соль, прованские травы, дрожжи.", "images/53afcf3235fe4b7f9e678219acfd87a4_donar_1.jpg"),
        (2, "Донар с говядиной", 23000.00, "Лаваш, говядина на гриле, салат айсберг, помидор свежий, лук репчатый, сыр эмменталь, соус.", "images/c06e28b0d3b0464e8c97692900132342_donar_3.jpg"),
        (6, "Кола", 5500.00, "Кола, лёд, вода", "images/7975867be1cf4112ae55ebde3519308c_water_2.jpg"),
        (6, "Коктейль из киви", 6000.00, "Киви отличается не только ярким цветом, ярким вкусом с легкой кислинкой. В нем содержится большое количество полезных элементов. Если включить киви в ежедневный рацион или просто употреблять в пищу чаще, вы поможете организму витаминами, которых, порой, так не хватает.", "images/e3eab4deae94447ca32e8e02e003ad84_water_3.jpg"),
        (3, "Хот-дог с сыром", 20000.00, "Булочки для хот-догов, Сосиски, Маринованные корнишоны, Майонез, Кетчуп,  Сыр", "images/97fc67d293e34b199b898801a676b005_hot-dog_1.jpg"),
        (4, "Эклер в шоколаде", 15000.00, "Традиционное французское пирожное из нежного заварного теста, которое наполнено легким заварным кремом и покрыто шоколадной глазурью", "images/998dfad817234b1a8c767ef419e3fc24_desert_1.jpg"),
        (4, "Канноли", 17000.00, "Канноли (cannoli), хрустящие трубочки с начинкой из рикотты и цукатов, — традиционный сицилийский десерт.", "images/259b1093a1b04e839fcc0f4c7916f23f_desert_2.jpg"),
        (4, "Брауни", 18000.00, "Брауни – очень известные американские пирожные с ярким и насыщенным шоколадным вкусом, плотной корочкой и влажной, слегка тягучей консистенцией внутри.", "images/260057fa83b54a0e9167f6c7709b5f57_desert_3.jpg"),
        (5, "Соус сырный", 2000.00, "Сырный соус станет вкусным дополнением ко многим блюдам. Он прекрасно сочетается с макаронами, овощами, рыбой и курицей.", "images/e2d53801e54e4d4583327a4babbb653a_sous_1.jpg"),
    )

    with Session(engine) as session:
        for category in categories:
            query = Categories(category_name=category)
            session.add(query)
        session.commit()

        for product in products:
            query = Products(
                category_id=product[0],
                product_name=product[1],
                price=product[2],
                description=product[3],
                image=product[4]
            )
            session.add(query)
        session.commit()


if __name__ == '__main__':
    main()

