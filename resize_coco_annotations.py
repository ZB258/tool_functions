import json
import argparse

def resize_coco_annotations(input_json_path, output_json_path, original_size=(640, 640), new_size=(256, 256)):
    with open(input_json_path, 'r') as f:
        data = json.load(f)

    original_width, original_height = original_size
    new_width, new_height = new_size
    width_ratio = new_width / original_width
    height_ratio = new_height / original_height

    for annotation in data['annotations']:
        # Adjust bounding box
        bbox = annotation['bbox']
        bbox[0] *= width_ratio  # x/home/jin/1_projects/detectron2/datasets/SARscope/annotations/test_annotations.coco.json
        bbox[1] *= height_ratio  # y
        bbox[2] *= width_ratio   # width
        bbox[3] *= height_ratio  # height
        annotation['bbox'] = bbox
        
        # Adjust area
        annotation['area'] = bbox[2] * bbox[3]  # width * height

        # Adjust segmentation if it exists
        if 'segmentation' in annotation:
            for segment in annotation['segmentation']:
                for i in range(0, len(segment), 2):
                    segment[i] *= width_ratio  # x
                    segment[i + 1] *= height_ratio  # y

    for image in data['images']:
        # Update image size
        image['width'] = new_width
        image['height'] = new_height

    with open(output_json_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize COCO annotations for a new image resolution.")
    parser.add_argument("--input_json", type=str, help="Path to the input COCO annotation JSON file.")
    parser.add_argument("--output_json", type=str, help="Path to save the resized COCO annotation JSON file.")
    parser.add_argument("--original_size", type=int, nargs=2, default=(640, 640), 
                        help="Original image size as two integers, e.g., 640 640")
    parser.add_argument("--new_size", type=int, nargs=2, default=(256, 256), 
                        help="New image size as two integers, e.g., 256 256")

    args = parser.parse_args()
    resize_coco_annotations(args.input_json, args.output_json, tuple(args.original_size), tuple(args.new_size))

