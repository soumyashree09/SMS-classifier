import csv
with open('spam.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    messages = [{'text': row['message'], 'label': row['label']} for row in csv_reader]
messages = [
    {'text': 'Hello, how are you?', 'label': 'ham'},
    {'text': 'Win a free iPhone now!', 'label': 'spam'},
]

# Splitting the data into training and testing sets
texts_train = [message['text'] for message in messages[:int(len(messages)*0.8)]]
labels_train = [message['label'] for message in messages[:int(len(messages)*0.8)]]
texts_test = [message['text'] for message in messages[int(len(messages)*0.8):]]
labels_test = [message['label'] for message in messages[int(len(messages)*0.8):]]

# Creating a bag-of-words model
word_counts_train = {}
for text in texts_train:
    words = text.lower().split()
    for word in words:
        if word not in word_counts_train:
            word_counts_train[word] = 1
        else:
            word_counts_train[word] += 1

# Training a Naive Bayes classifier
spam_words_count = {}
ham_words_count = {}
for text, label in zip(texts_train, labels_train):
    words = text.lower().split()
    for word in words:
        if label == 'spam':
            spam_words_count[word] = spam_words_count.get(word, 0) + 1
        else:
            ham_words_count[word] = ham_words_count.get(word, 0) + 1

# Making predictions on the test set
predictions = []
for text in texts_test:
    spam_score = 0
    ham_score = 0
    words = text.lower().split()
    for word in words:
        spam_score += spam_words_count.get(word, 0)
        ham_score += ham_words_count.get(word, 0)
    if spam_score > ham_score:
        predictions.append('spam')
    else:
        predictions.append('ham')

# Evaluating the model
correct_predictions = sum(1 for pred, label in zip(predictions, labels_test) if pred == label)
accuracy = correct_predictions / len(predictions)

# Print the results
print(f"Accuracy: {accuracy:.2f}")