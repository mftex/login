from Model import Usuario
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

# Instacia a sessão com BD
def retorna_session():
    USUARIO = 'root'
    SENHA = 'asdasd'
    HOST = 'localhost'
    BANCO = 'login'
    PORTA = '3306'
    CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}'
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

# Cadastro de usuários
class ControllerCadastro():
    # Validações de nome, email e senha informados
    @classmethod
    def verificaDados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        
        return 1
    
    # Inserção dos dados em banco
    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()
        usuario = session.query(Usuario).filter(Usuario.email == email).all()

        # Se já existir usuário, retorna valor erro 5 e para execução do método
        if len(usuario) > 0:
            return 5
        
        # Chama as validações de nome, email e senha. 
        dados_verificados = cls.verificaDados(nome, email, senha)
        if dados_verificados != 1:
            return dados_verificados

        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            u1 = Usuario(nome=nome, email=email, senha=senha)
            session.add(u1)
            session.commit()
            return 1
        except:
            return 3

# Classe para validar login
class ControllerLogin():
    @classmethod
    def verificaLogin(cls, email, senha):
        session = retorna_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        # Preenche 'logado' se encontrar usuário e senha informados
        logado = session.query(Usuario).filter(Usuario.email == email).filter(Usuario.senha == senha).all()
        
        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False
