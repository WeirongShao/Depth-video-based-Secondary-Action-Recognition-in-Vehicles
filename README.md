<div align="center">
<h1> Depth-video based Secondary Action Recognition in Vehicles via CNN and Bi-LSTM with Spatial Enhance Attention Mechanism </h1>


[Weirong Shao](https://www.linkedin.com/in/weirong-shao-224a41155/)</a><sup><span>1*</span></sup>, 
Mondher Bouazizi</a><sup><span>2</span></sup>,
Ohtsuki Tomoaki</a><sup><span>3*</span></sup>,
</br>

<sup>1</sup> Graduate School of Science and Technology, Keio University, Yokohama 223-8522, Japan.
<sup>*</sup> Corresponding author.
<br>
<div>

<img src="images/input_example_.jpg" width=60%>

</div>
</div>

# 📎 Abstract
Secondary actions in vehicles are activities that drivers engage in while driving that are not directly related to the primary task of operating the vehicle. Secondary Action Recognition (SAR) in drivers is vital for enhancing road safety and minimizing accidents related to distracted driving. It also plays an important part in modern car driving systems such as Advanced Driving Assistance Systems (ADAS), as it helps identify distractions and predict the driver's intent. Traditional methods of action recognition in vehicles mostly rely on RGB videos, which can be significantly impacted by external conditions such as low light levels. In this research, we introduce a novel method for SAR. Our approach utilizes depth-video data obtained from a depth sensor located in a vehicle. Our methodology leverages the Convolutional Neural Network (CNN), which is enhanced by the Spatial Enhanced Attention Mechanism (SEAM) and combined with Bidirectional Long Short-term Memory (Bi-LSTM) networks. This method significantly enhances action recognition ability in depth videos by improving both spatial and temporal aspects. We conduct experiments using K-fold cross-validation, and the experimental results show that on the public benchmark dataset [**Drive&Act**](https://arxiv.org/pdf/2203.00927.pdf)], our proposed method shows significant improvement in SAR compared to the state-of-the-art methods, reaching an accuracy of about 84% in SAR in depth videos.

# News
This work is accepted to [[**MDPI sensors**](https://www.mdpi.com/1424-8220/24/20/6604)]

## Extract videos clips 
We use the publicly available dataset [[**Drive&Act**](https://arxiv.org/pdf/2203.00927.pdf)] and Act & Drive datasets in our work. For training and testing the models, place the dataset files in the correct directories like shown below.
