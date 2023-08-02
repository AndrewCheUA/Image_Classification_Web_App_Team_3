# IMAGE CLASSIFICATION WEB APP

###### 🔗 team_3 image classification app
[press it](https://hub.docker.com/layers/andriiche/ml_team3_test/latest/images/sha256-e7933cab4040994cea4cb8996153e7138b2df5fa709772e7ae5d81dc6c5aa754?context=repo)


## TOPICS

1. What it does 
2. Functionality
3. Machine Learning Process
4. Model Architecture
5. Results
6. How we built it
7. Challenges we ran into
8. What we learned
9. Installing and Running Locally
10. Used By
11. Authors


## 💻 What it does

The TEAM_3 made this APP as part of the GoIT course training.

Image Classification is a tool that utilizes the power of Deep Learning to distinguish various photos and categorize them by 10 classes. Image Classification will tag it accordingly to the class it belongs to. Simply submit the image, and the machine learning model will evaluate it and provide a response in a fraction of a second.

## 📝 Functionality

The web application has 4 pages:
####
###### - WebML-app: The main page provides brief information about the developers of the project and the neural network
####
###### - Predict: In the <Download picture> field, you need to insert the picture of your choice. Then press the <predict> button. After that, the picture is transferred to the neural network and gives the result.
####
###### Model Data: This is a page that displays brief information about the neural network
####
###### GPT Clone: Chat GPT clone.


## 🤖 Machine Learning Process

<h3> 📊 Getting the Data and EDA Process </h3>

_The dataset was taken from Kaggle and you can find it [Cifar10](https://telegra.ph/Sifar10-03-28)._<br>

The Dataset consists of 60000 32x32 color images divided into 10 classes, each with 6000 images.  Each image belongs to one of ten categories: airplane, car, bird, cat, deer, dog, frog, horse, ship, or truck


### ⚙️ Model Architecture

![image](https://github.com/OlgaNazarenko/Different/assets/113229061/9e99289e-6e41-4d03-a8d6-ee0ff385371b)

The model is a Sequential Model consisting of a total of 5 Convolutional Layers and 4 Dense Layers.

The first Convolutional Layer starts with 32 filters and uses a kernel size of 2x2.
Subsequent Convolutional Layers double the number of filters and increment the kernel size by 1 at each layer.
To prevent overfitting and reduce computational costs, Max Pooling Layers are introduced after some of the Convolutional Layers.

After the last Convolutional Layer, the output is flattened and passed to the Dense Layers.

The first Dense Layer contains 512 neurons, and the number of neurons is halved over the next two Dense Layers.
Throughout the model, Dropout Layers are added to randomly ignore some neurons during training and mitigate overfitting.

ReLU activation is used in all layers except for the output layer. ReLU helps introduce non-linearity and reduces the computation cost.

The Output Layer has 2 neurons, one for each class in the classification task, and uses softmax activation to provide probability scores for each class.

Overall, the architecture is designed to extract relevant features through convolutional layers, reduce dimensions through pooling, and make the final classification decision through dense layers and softmax activation. Dropout layers are incorporated to enhance the model's generalization ability and prevent overfitting.

<img width="581" alt="Screenshot 2023-08-02 at 19 19 24" src="https://github.com/OlgaNazarenko/Different/assets/113229061/8f74fa4d-ff0a-4dd2-a3ea-545177b2b62d" align="right"  width="30%"/>
<img width="580" alt="Screenshot 2023-08-02 at 19 18 35" src="https://github.com/OlgaNazarenko/Different/assets/113229061/ed8ca001-62a2-4f65-afd6-0d63070fa32d" align="right"  width="30%"/>

### 🤩 Results

- The model with the least Validation Loss was saved during the training and reloaded before obtaining the final results.
- The model was able to classify the most of samples correctly. Some of them, if include several objects, can identify one of them correctly.

## ⚙️ How we built it

- Streamlit: For backend and frontend
- Python: For backend
- HTML: For frontend
- GitHub pages: For CI/CD and deployment

## 🧠 Challenges we ran into

After achieving 87% accuracy on the testing data initially, we were relieved thinking we have built something great that can correctly classify most of the fake images online, but we wanted to improve and don't stop of what we got. All of us had been working on our models. We decided to put it to the test by downloading more test images from Google, but the results were good, but some of them were utterly unexpected, like for a bird it could recognise it as an airplane. It was logical and similar, but still were expected to have more precise results. Some photos we evaluated were incorrectly categorized. We were so disappointed with the outcome that we decided to improve and implement a little different strategy, and it worked like magic.

## 📖 What we learned

- The power of Deep Learning is that it can be used to classify images in a very fast and accurate manner.
- Working and deploying a model on the cloud.
- Deploying web app on GitHub Pages.
- Efficient use of GitHub actions.

## 🏃🏻‍♂️ Installing and Running Locally

Yot can download our web app docker container and use it:

```bash
  docker pull andriiche/ml_team3_test:latest
```
```bash
  docker run -it -d -p 80:80 ml_team3_test:latest
```

## 🤝 Used By

This project is used by:

- GoIT
- Google
- Tim Cook

## 🕵 Authors:

- [@AndrewCheUA ](https://github.com/AndrewCheUA?tab=repositories)
- [@Serhii-Kravchenko-2022  ](https://github.com/Serhii-Kravchenko-2022?tab=repositories)
- [@Igor-Mozharov ](https://github.com/Igor-Mozharov?tab=repositories)
- [@OlgaNazarenko ](https://github.com/OlgaNazarenko?tab=repositories)

## 📣 Feedback

If you have any feedback, please reach out to us at dream-team_3@fake.ua

#
# Glory to Ukraine !


