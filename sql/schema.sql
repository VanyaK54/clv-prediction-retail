-- Database: RetailCLV

-- Table to store customer master info
CREATE TABLE Customers (
    CustomerID VARCHAR(20) PRIMARY KEY,
    Gender CHAR(1),
    Age INT,
    Country VARCHAR(50),
    SignupDate DATE
);

-- Table to store transaction-level summary
CREATE TABLE CustomerTransactions (
    TransactionID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID VARCHAR(20) FOREIGN KEY REFERENCES Customers(CustomerID),
    LastPurchaseDate DATE,
    TotalPurchases INT,
    TotalRevenue DECIMAL(10, 2),
    AvgOrderValue DECIMAL(10, 2)
);

-- Table to store behavioral metrics
CREATE TABLE CustomerBehavior (
    BehaviorID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID VARCHAR(20) FOREIGN KEY REFERENCES Customers(CustomerID),
    WebsiteVisits INT,
    EmailClicks INT
);

-- Table to store CLV predictions
CREATE TABLE CLVPredictions (
    PredictionID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID VARCHAR(20) FOREIGN KEY REFERENCES Customers(CustomerID),
    Recency INT,
    Frequency INT,
    Monetary DECIMAL(10,2),
    TenureDays INT,
    ClicksPerVisit FLOAT,
    RevenuePerVisit FLOAT,
    CountryEncoded INT,
    GenderEncoded INT,
    PredictedCLV DECIMAL(12,2),
    PredictionDate DATETIME DEFAULT GETDATE()
);
