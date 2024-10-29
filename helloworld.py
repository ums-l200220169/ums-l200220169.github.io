from metaflow import FlowSpec, step

class HelloWorldFlow(FlowSpec):

    @step
    def start(self):
        print("Hello, World!")
        self.next(self.end)

    @step
    def end(self):
        print("Goodbye, World!")

if __name__ == "__main__":
    HelloWorldFlow()

