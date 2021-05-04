
class model(torch.nn.Module):
    def __init__(self):
        super(model, self).__init__()
        self.fc1 = nn.Linear(len(offensive_columns),5)
        self.fc2 = nn.Linear(5,1)
        self.fc3 = nn.Linear(len(defensive_columns),5)
        self.fc4 = nn.Linear(5,1)
        
        self.bn1 = nn.BatchNorm1d(5)
        self.bn2 = nn.BatchNorm1d(5)
        
        self.relu = torch.nn.ReLU() # instead of Heaviside step fn
    
    def offensive_rating(self, x):
        x = self.fc1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        return x
    
    def defensive_rating(self, x):
        x = self.fc3(x)
        x = self.bn2(x)
        x = self.relu(x)
        x = self.fc4(x)
        x = self.relu(x)
        return x
    
    def forward(self, x_h_a, x_h_d, x_a_a, x_a_d):
        r_h_a = self.offensive_rating(x_h_a)
        r_a_d = self.defensive_rating(x_a_d)
        r_a_a = self.offensive_rating(x_a_a)
        r_h_d = self.defensive_rating(x_h_d)
        
        p1 = 1.5438116100766703 * r_h_a * r_a_d
        p2 = 1.17907995618839 * r_a_a * r_h_d
        
        return torch.cat((p1, p2), 1)
