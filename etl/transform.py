
def normalize_data(data):
    brand_map = {}
    brand_id_counter = 1

    brands = []
    computers = []
    cpus = []
    memory_modules = []
    storage_devices = []
    gpus = []

    for comp in data:
        comp_brand = comp["brand"]
        if comp_brand not in brand_map:
            brand_map[comp_brand] = brand_id_counter
            brands.append({"id": brand_id_counter, "name": comp_brand})
            brand_id_counter += 1

        comp_id = comp["id"]
        computers.append({
            "id": comp_id,
            "brand_id": brand_map[comp_brand],
            "model": comp["model"],
            "os": comp["os"]
        })

        cpus.append({
            "computer_id": comp_id,
            **comp["cpu"]
        })

        memory_modules.append({
            "computer_id": comp_id,
            **comp["memory"]
        })

        for storage in comp["storage"]:
            storage_devices.append({
                "computer_id": comp_id,
                **storage
            })

        gpus.append({
            "computer_id": comp_id,
            **comp["gpu"]
        })

    return {
        "brands": brands,
        "computers": computers,
        "cpus": cpus,
        "memory_modules": memory_modules,
        "storage_devices": storage_devices,
        "gpus": gpus
    }
