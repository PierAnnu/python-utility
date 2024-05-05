# coding=utf-8

#version 0.0
#--------------------------------------------------
#Updates
#0.0 - Initial file version
#--------------------------------------------------
#Description
#Image Helper function
#--------------------------------------------------

import cv2
import numpy as np


def find_image_coords(complete_image_path,piece_to_find_path):
  ''' Cerca un pezzo di immagine in un'immagine completa.
  args: @complete_image_path: str: path dell'immagine completa
        @piece_to_find_path : str: path del pezzo di immagine da cercare nell'immagine completa
        
  return:
        tuple: coords (x,y) coordinate dell'immagine identificata '''
  img_rgb = cv2.imread(complete_image_path)
  template = cv2.imread(piece_to_find_path)
  w, h = template.shape[:-1]

  res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
  threshold = .98
  loc = np.where(res >= threshold)
  points = []
  for pt in zip(*loc[::-1]):  # Switch columns and rows
    points.append((pt[0],pt[1]))
    # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
  return points[0]


# coords = find_image_coords(r"./image1.png",r"./image2.png")
# print(coords)