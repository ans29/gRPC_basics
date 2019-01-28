import grpc
import evaluator_pb2
import evaluator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = evaluator_pb2_grpc.EvaluatorStub(channel)

#take input from user
infix = raw_input("Enter an infix expression : ")

# create a valid request message
exp_to_solve = evaluator_pb2.Expr(str_exp=infix)

# make the call
response = stub.Eval(exp_to_solve)
print(response.output)