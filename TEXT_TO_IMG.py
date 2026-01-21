import torch
from diffusers import StableDiffusionPipeline

def generate_image(prompt, output_path="generated_image.png"):
    # Load Stable Diffusion model from Hugging Face (run once, downloads model)
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    
    # Use CPU or CUDA if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = pipe.to(device)

    print(f"Generating image for: {prompt}")
    image = pipe(prompt).images[0]  # Get first generated image
    image.save(output_path)
    print(f"Image saved as {output_path}")

# Example prompt
generate_image("a futuristic city skyline at sunset, high detail, digital art")
