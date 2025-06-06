class Armor:
    def __init__(self,
                name: str,
                hp: int,
                id: int,
                drawback: int
                ) -> None:
        self.name = name
        self.hp = hp
        self.id = id
        self.drawback = drawback

chainmail = Armor(name="Chainmail", hp=25, id=0, drawback=0)
light_armor = Armor(name="Light Armor", hp=50, id=1, drawback=0)
heavy_armor = Armor(name="Heavy Armor", hp=100, id=2, drawback=3)