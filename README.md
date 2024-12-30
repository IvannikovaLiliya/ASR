# Automatic Speech Recognition (ASR) with PyTorch

<p align="center">
  <a href="#about">About</a> •
  <a href="#installation">Installation</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## About

This repository contains a template for solving ASR task with PyTorch. This template branch is a part of the [HSE DLA course](https://github.com/markovka17/dla) ASR homework. 

## Installation

Follow these steps to install the project:

0. `conda` version:

   ```bash
   # create env
   conda create -n project_env python=python3.9

   # activate env
   conda activate project_env
   ```

1. Install all required packages

   ```bash
   pip install -r requirements.txt
   ```

2. Install the best model checkpoint

   ```bash
   sh ./download_best_model.sh
   ```

## Inference of model

   python inference.py

## Train the model

   python train.py

## Experimets

   [HSE ASR HW](https://api.wandb.ai/links/bubbo777125-bauman-moscow-state-technical-university/55ldqaea)
