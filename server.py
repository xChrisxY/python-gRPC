import grpc 
from concurrent import futures
import greeter_pb2
import greeter_pb2_grpc

# [+] Implementamos la lógica del servicio
class GreeterService(greeter_pb2_grpc.GreeterServicer):
    
    def SayHello(self, request, context):
        return greeter_pb2.HelloResponse(message=f"!Hola, {request.name}")

        
def run_server():
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("[::]:50051")
    print("Servidor iniciado en el puerto 50051")
    server.start()
    server.wait_for_termination()
    

if __name__ == '__main__':
    run_server()











