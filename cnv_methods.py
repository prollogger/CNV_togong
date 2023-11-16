import ifcopenshell
import tkinter as tk
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
from tkinter import filedialog
import re
import os
import subprocess
import itertools
import cnv_methods as cnv

import json

def get_material_names(ifc_object):
    ##나중에 쓸것
    # 재료 이름들을 저장할 리스트를 만듭니다.
    material_names = []
    
    # 여기에 ifc_object에서 재료 정보를 추출하는 코드를 작성합니다.
    # 아래는 예시 코드입니다.
    if hasattr(ifc_object, 'HasAssociations'):
        for association in ifc_object.HasAssociations:
            if association.is_a('IfcRelAssociatesMaterial'):
                material_select = association.RelatingMaterial
                # 재료가 단일 재료인 경우
                if material_select.is_a('IfcMaterial'):
                    material_names.append(material_select.Name)
                # 재료가 여러 개인 경우 (예: IfcMaterialList, IfcMaterialLayerSet)
                elif material_select.is_a('IfcMaterialList') or material_select.is_a('IfcMaterialLayerSet'):
                    for material in material_select.MaterialLayers:
                        material_names.append(material.Material.Name)
                # 다른 재료 관련 엔티티에 대한 처리를 추가할 수 있습니다.
                
    # 모든 재료 이름을 쉼표로 구분한 문자열로 합칩니다.
    return ", ".join(material_names)


def select_folder():


    folder_path = filedialog.askdirectory()
    return folder_path + "/"

    


def save_json(data,file_path):
# 예시 JSON 데이터 (리스트)
    # JSON 데이터를 파일로 저장
    with open(file_path, 'w') as file:
        json.dump(data, file)


def load_json(file_path):
# 파일에서 JSON 데이터 불러오기
    with open(file_path, 'r') as file:
        loaded_data = json.load(file)

    return loaded_data


def load_template():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("템플릿파일(JSON)", "*.json"),
                                          ("all files", "*.*")))
    with open(os.path.join("filepath.txt"), "w", encoding="utf-8") as f:
                f.write(os.path.normpath(filename))
    return filename


def open_ifc(filename):
    return ifcopenshell.open(filename)
     


def ifcwall_data_object(model):
    #-------------------------------------------------------------------------------------------------------
    walls = model.by_type("IfcWall")
    #-------------------------------------------------------------------------------------------------------

    object_list = []

    for wall in walls:
        wall_type = ifcopenshell.util.element.get_type(wall)
        wall_type_mat_set = ifcopenshell.util.element.get_material(wall_type)
        layer_sequence = wall_type_mat_set.MaterialLayers


        global_id = ""
        try:    
            global_id = wall.get_info()['GlobalId']
        except Exception as e:
            global_id = ""

        length = ""
        try:    
            length = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['Length']
        except Exception as e:
            length = ""

        width = ""
        try:    
            width = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['Width']
        except Exception as e:
            width = ""

        height = ""
        try:    
            height = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['Height']
        except Exception as e:
            height = ""

        gross_footprint_area = ""
        try:    
            gross_footprint_area = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['GrossFootprintArea']
        except Exception as e:
            gross_footprint_area = ""

        net_footprint_area = ""
        try:    
            net_footprint_area = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['NetFootprintArea']
        except Exception as e:
            net_footprint_area = ""

        gross_side_area = ""
        try:    
            gross_side_area = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['GrossSideArea']
        except Exception as e:
            gross_side_area = ""

        net_side_area = ""
        try:    
            net_side_area = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['NetSdieArea']
        except Exception as e:
            net_side_area = ""

        gross_volume = ""
        try:    
            gross_volume = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['GrossVolume']
        except Exception as e:
            gross_volume = ""

        net_weight = ""
        try:    
            net_weight = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['NetWeight'] 
        except Exception as e:
            net_weight = ""

        gross_weight = ""
        try:    
            gross_weight = ifcopenshell.util.element.get_psets(wall)['Qto_WallBaseQuantities']['GrossWeight'] 
        except Exception as e:
            gross_weight = ""




        for layer_sequence_number, layer in enumerate(layer_sequence):
            
   
            material = layer.Material.Name if layer.Material else 'Unknown Material'
  
            
            objectDataJson = {"GlobalId":global_id,
                            "MaterialLayer":layer_sequence_number,
                            "Material":material,
                            "cnvcode":global_id+"-"+str(layer_sequence_number)+"-"+material,
                            "MaterialLayerThickness":layer.LayerThickness,
                            "Length":length,
                            "Width":width,
                            "Height":height,
                            "GrossFootprintArea":gross_footprint_area,
                            "NetFootprintArea":net_footprint_area,
                            "GrossSideArea":gross_side_area,
                            "NetSideArea":net_side_area,
                            "GrossVolume":gross_volume,
                            "GrossWeight":gross_weight,
                            "NetWeight":net_weight,
                            }
            object_list.append(objectDataJson)
    return object_list    

import ifcopenshell

def get_area_from_object_quantity_set(ifc_file_path, object_global_id):
    
    
    try:
        # IFC 파일을 엽니다.
        
        
        ifc_file = ifcopenshell.open(ifc_file_path)

        # 해당 GlobalId를 가진 객체를 찾습니다.
        ifc_object = ifc_file.by_guid(object_global_id)
        if not ifc_object:
            return 0

        # 객체와 연관된 모든 Quantity Sets를 검색합니다.
        for quantity_set in ifc_object.IsDefinedBy:
            if quantity_set.is_a("IfcRelDefinesByProperties"):
                properties = quantity_set.RelatingPropertyDefinition
                if properties.is_a("IfcElementQuantity"):
                    for quantity in properties.Quantities:
                        # 'Area' 수량을 찾습니다.
                        if quantity.is_a("IfcQuantityArea"):
                            return quantity.AreaValue

        # 'Area' 수량이 없는 경우
        return 0
    except:
        return 0
