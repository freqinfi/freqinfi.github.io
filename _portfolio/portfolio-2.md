---
title: "Mechatronics Project"
excerpt: "Face recognition coffee machine<br/><img src='/images/mecha_logo.png' width='500' height='300'>
"
collection: portfolio
---


<br>
<span style = "font-size:16px; color: gray;"> 현대 인프라코어의 지원으로 대회 형식으로 개최된 메카트로닉스 과목 Final Project에 대한 내용</span>
<br><br>

<img src='/images/mecha_prize.jpg' width = 300 height = 500/>

* <strong style = "color: blue; font-size:22px;">Introduction</strong><br>
    <span style = "font-size:16px; color: gray;"><br> 
    얼굴인식과 같은 생체인식은 사람이 항상 사용할 수 있다. 이러한 특성을 이용하여 사람들은 쉽게 다른 사람과 자신을 구별할 수 있으며, 이를 통해서 그 사람에게만 개인화된 서비스를 제공할 수 있는 특성이 있습니다.
    </span><br><br><span style = "font-size:16px; color: gray;">
    이러한 특성을 활용하여 회사나 공공기관 등의 고정된 이용자를 가진 집단에서 간식이나 음료 등을 핸드폰을 통해서 자신의 선호를 결정하고 이를 반영하여 제공할 수 있는 서비스에 대해서 고안해보았습니다.
    </span><br><br><span style = "font-size:16px; color: gray;">
    간식 / 음료를 모두 포함한 자판기를 설계하는 것에 한계가 있기 때문에 4가지 음료를 조합하여 자신이 원하는 비율로 설정하고, 얼굴인식을 통해 원하는 음료를 받을 수 있는 음료자판기를 만들어 보았습니다.
    </span><br><br>


* <strong style = "color: blue; font-size:22px;">Mechanism</strong><br>
    <span style = "font-size:16px; color: gray;"><br> 
    1. 사용자가 Web App을 통해서 자신의 사진을 등록하며 가입하고, 음료 recipe(음료의 비율)을 추가할 수 있다. 이러한 정보를 API를 통해 Python에서 읽을 수 있도록 제공한다.
    </span><br><br><span style = "font-size:16px; color: gray;">
    2. 라즈베리파이 4 환경에서 Python을 구동하여 카메라를 이용하여 얼굴을 촬영하고, 등록된 사용자들의 사진과 비교하여 얼굴인식을 수행한다. 인식된 사용자에 해당하는 음료 비율로 각각의 음료를 몇 초동안 따를 것인지 계산하고, 이를 Arduino로 전송한다.
    </span><br><br><span style = "font-size:16px; color: gray;">
    3. Arduino로 초음파센서, 서보모터, LED를 제어하여 사용자의 선호에 맞는 비율로 음료를 제공한다. 이때 초음파센서가 컵을 인식하였을 때만 음료를 제공하도록 설계하여 오작동을 배제한다.
    </span><br><br>

<img src='/images/mecha.png'/>


* 응애

    * [Material](/files/StereoDepthEstimation/2023-S UROP.pdf)
    * <strong> Contents</strong>
        * Manufacturing Camera System
        * Camera System Assembly
        * Basic of 3D computer vision


