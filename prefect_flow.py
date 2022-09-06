from prefect import flow

@flow
def testing():
    print("flow ran, yay!")