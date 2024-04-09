import matplotlib.pyplot as plt

# Data
models = ['SVM', 'CNN']
accuracies = [78, 97]  # Accuracy values corresponding to each model

# Plotting the bar graph
plt.figure(figsize=(8, 6))
plt.bar(models, accuracies, color=['blue', 'green'])

# Adding title and labels
plt.title('Accuracy for abnormal')
plt.xlabel('Model')
plt.ylabel('Accuracy (%)')

plt.ylim(0, 100)  
plt.show()