import grpc
from concurrent import futures 
import users_pb2
import users_pb2_grpc
import uuid 

users_db = {}

class UserService(users_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        user_id = str(uuid.uuid4())
        user = users_pb2.User(id=user_id, name=request.name, email=request.email)
        users_db[user_id] = user 
        return users_pb2.UserResponse(user=user)

    def GetUserById(self, request, context):
        user = users_db.get(request.id)
        if user:
            return users_pb2.UserResponse(user=user)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("User not found")
        return users_pb2.UserResponse()
    
def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    print("Servidor iniciado en el puerto 50051")
    server.start()
    server.wait_for_termination()
    
if __name__ == '__main__':
    run_server()