import grpc
from concurrent import futures
import time

# import the generated classes
import evaluator_pb2
import evaluator_pb2_grpc

# import the original evaluator.py
import evaluator

# create a class to define the server functions, derived from
#evaluator_pb2_grpc.EvaluatorServicer
class EvaluatorServicer(evaluator_pb2_grpc.EvaluatorServicer):

    # evaluator.eval_expr is exposed here
    # the request and response are of the data type
    # evaluator_pb2.Expr
    def Eval(self, request, context):
        response = evaluator_pb2.Expr()
        response.output = evaluator.eval_expr(request.str_exp)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_EvaluatorServicer_to_server`
# to add the defined class to the server
evaluator_pb2_grpc.add_EvaluatorServicer_to_server(
        EvaluatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
