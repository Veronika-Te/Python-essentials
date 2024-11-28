import asyncio
import json
from aiofile import async_open

async def parse_json(file_path):
    """Parsing JSON"""
    try:
        async with async_open(file_path, "r") as file:
            content = await file.read()  # Asynchronously read file content
            data = json.loads(content)  # Parse JSON content
            
        user_names=[]
        total_purchase=[]
        for user in data:
            user_names.append(user.get('name'))
            total= user.get('purchases')
            for ele in total:
                total_purchase.append(ele)
        print(f"Total purchases are {total_purchase}")
        return user_names
        
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file '{file_path}'")
    except asyncio.CancelledError:
        raise RuntimeError("The asynchronous task was cancelled")
    except Exception as e:
        raise ValueError(f"An error occurred while parsing JSON from '{file_path}': {e}")

async def main(): 
    
    #etracted_data=await asyncio.gather(parse_json(json_file)
    json_file = 'users_data.json'
    json_file2= 'users_data2.json'
    print(f"Reading file: {json_file}")
    try:
        extracted_data = await asyncio.gather(parse_json(json_file), parse_json(json_file2))
        print("Extracted Data (Names of users):", extracted_data)
    except asyncio.TimeoutError:
        print(f"Error: The operation timed out while reading {json.file}")
    except Exception as e:
        print(f"Error: {e}")

 
if __name__=="__main__":
    asyncio.run(main())
