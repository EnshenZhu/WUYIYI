import torch
import torch.nn as nn

class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()

        self.hidden_size = hidden_size

        # Define the RNN layer
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)

        # Define the fully connected layer
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # Initialize hidden state with zeros
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)

        # Forward pass through the RNN layer
        out, _ = self.rnn(x, h0)

        # Take the output from the last time step
        out = self.fc(out[:, -1, :])

        return out

# Example usage
input_size = 10
hidden_size = 20
output_size = 5

# Create an instance of the SimpleRNN model
model = SimpleRNN(input_size, hidden_size, output_size)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Dummy input data
dummy_input = torch.randn((32, 15, input_size))  # Batch size: 32, Sequence length: 15

print(dummy_input[0].shape)

# Forward pass
output = model(dummy_input)

# Print the model architecture and output shape
print(model)
print("Output shape:", output.shape)