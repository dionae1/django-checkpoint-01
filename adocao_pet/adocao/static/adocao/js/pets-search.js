document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("pet-search-input");

    if (!searchInput) {
        return;
    }

    const petItems = Array.from(document.querySelectorAll("[data-pet-name]"));
    const emptyState = document.getElementById("pet-search-empty");

    const normalizeText = (value) =>
        value
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .trim();

    const filterPets = () => {
        const query = normalizeText(searchInput.value);
        let visibleCount = 0;

        petItems.forEach((item) => {
            const name = normalizeText(item.getAttribute("data-pet-name") || "");
            const shouldShow = query === "" || name.includes(query);

            item.classList.toggle("d-none", !shouldShow);

            if (shouldShow) {
                visibleCount += 1;
            }
        });

        if (emptyState) {
            emptyState.classList.toggle("d-none", visibleCount !== 0);
        }
    };

    searchInput.addEventListener("input", filterPets);
});
