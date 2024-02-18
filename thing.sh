#!/bin/bash

# Define an array of directories
directories=(
    "amalfi-coast"
    "aquarium-nyc"
    "art-museum"
    "backward-jogger"
    "basketball-explosion"
    "big-eyed-fluff-ball"
    "big-sur"
    "birds-over-river"
    "cat-on-bed"
    "chair-archaeology"
    "chameleon"
    "chinese-new-year-dragon"
    "closeup-man-in-glasses"
    "closeup-of-womans-eye"
    "cloud-man"
    "dancing-kangaroo"
    "dogs-downtown"
    "flower-blooming"
    "gold-rush"
    "grandma-birthday"
    "happy-cat"
    "italian-pup"
    "lagos"
    "man-on-the-cloud"
    "mitten-astronaut"
    "monster-with-melting-candle"
    "octopus-and-crab"
    "origami-undersea"
    "otter-on-surfboard"
    "paper-airplanes"
    "petri-dish-pandas"
    "photoreal-train"
    "puppy-cloning"
    "robot-video-game"
    "santorini"
    "ships-in-coffee"
    "snow-dogs"
    "stack-of-tvs"
    "suv-in-the-dust"
    "tiny-construction"
    "tokyo-in-the-snow"
    "tokyo-walk"
    "train-window"
    "victoria-crowned-pigeon"
    "vlogger-corgi"
    "wolves"
    "wooly-mammoth"
    "zen-garden-gnome"
)

# Loop through each directory
for dir in "${directories[@]}"; do
    # Check if both directories exist
    if [ -d "normal_frames/$dir" ] && [ -d "interpolated_frames/${dir}_processed_8x" ]; then
        echo "Processing $dir..."
        python -m pytorch_fid normal_frames/"$dir" interpolated_frames/"${dir}_processed_8x"
    else
        echo "Skipping $dir: directory not found in either normal_frames or interpolated_frames."
    fi
done
