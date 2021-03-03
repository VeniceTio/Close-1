class Articles:
    """Classe définissant un article caractérisée
     - id
     - nom
     - prix
     - quantite dispo
     - seller
     """

    def __init__(self, p_id=-1, p_name="Unamed", p_price=-1,
                 p_avaProd=-1, p_seller="Unamed", p_desc="unamed"):
        self.id = p_id
        self.name = p_name
        self.price = p_price
        self.AvailableProduct = p_avaProd
        self.seller = p_seller
        self.desc = p_desc

    def __getattr__(self, nom):
        ...
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
              cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

    def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""
        object.__setattr__(self, nom_attr, val_attr)
        self.enregistrer()

    def setName(self, p_name):
        self.name = p_name

    def setPrice(self, p_price):
        self.price = p_price

    def setAvaProd(self, p_number):
        self.AvailableProduct = p_number

    def setSeller(self, p_seller):
        self.seller = p_seller

    def setDesc(self, p_desc):
        self.desc = p_desc

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDesc(self):
        return self.desc

    def getSeller(self):
        return self.seller

    def getAvaProd(self):
        return self.AvailableProduct
