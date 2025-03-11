import grpc
import users_pb2
import users_pb2_grpc

def run():
    
    channel = grpc.insecure_channel("localhost:50051")
    stub = users_pb2_grpc.UserServiceStub(channel)
    
    print("[+] Creamos un usuario...")
    try:
        response = stub.CreateUser(users_pb2.CreateUserRequest(name="Chris", email="chris@gmail.com"))
        user_id = response.user.id
        print("Usuario creado %s" % (user_id))
        print("Nombre del usuario: %s" % (response.user.name))
        print("Email del usuario: %s" % (response.user.email))
    except grpc.RpcError as e:
        print(f"Error al crear el usuario {e.details()}")

    
    print("\n[+] Obteniendo usuario por ID...")
    try:
        response = stub.GetUserById(users_pb2.GetUserByIdRequest(id=user_id))
    except grpc.RpcError as e:
        print(f"Error al obtener el usuario: {e.details()}")

    print("El usuaruo obtenido es :", response.user)
    
if __name__ == '__main__':
    run()
    