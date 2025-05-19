/// ! **Project**   image_converter  
/// ! **Author**    Ezekiel A. Mitchell  
/// ! **Date**      2025-05-18  
/// ! **Repository** https://github.com/ezekielmitchell/ComputerVision/Projects/image_converter
/// !
/// ! ## Overview
/// ! Convert images between popular formats with high performance and minimal dependencies.
/// !
/// ! ## Features
/// ! - High-speed conversions  
/// ! - Support for PNG, JPEG, GIF, BMP, and more  
/// ! - Zero-cost abstractions and minimal dependencies  
/// ! - Simple, intuitive command-line interface

use clap::Parser;
use image::ImageError;
use std::path::PathBuf;

/// A simple program to convert images to grayscale
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Input image file path
    #[arg(short, long)]
    input: PathBuf,

    /// Output image file path
    #[arg(short, long)]
    output: Option<PathBuf>,
}

fn main() -> Result<(), ImageError> {
    let args = Args::parse();
    
    // Generate default output path if not provided
    let output_path = match args.output {
        Some(path) => path,
        None => {
            let stem = args.input.file_stem().unwrap_or_default();
            let parent = args.input.parent().unwrap_or_else(|| std::path::Path::new(""));
            parent.join(format!("{}_grayscale.png", stem.to_string_lossy()))
        }
    };

    println!("Converting {} to grayscale...", args.input.display());

    // Load the image
    let img = image::open(&args.input)?;

    // Convert to grayscale
    let gray_img = img.grayscale();

    // Save the grayscale image
    gray_img.save(&output_path)?;

    println!("Grayscale image saved to: {}", output_path.display());
    Ok(())
}