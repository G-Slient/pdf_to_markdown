"""

Dependencies
-------------
PyMuPDF v1.24.2 or later
"""

try:
    import pymupdf as fitz  # available with v1.24.3
except ImportError:
    import fitz


def compute_header_footer_coordinates(page):
    """
    Compute the coordinates of the header and footer on a given page.

    Args:
        page (PyMuPDF.Page): The page object representing the PDF page.

    Returns:
        tuple: A tuple containing the coordinates of the header and footer.
            The header coordinates are represented as (x0, y0, x1, y1),
            where (x0, y0) is the top-left corner and (x1, y1) is the bottom-right corner.
            The footer coordinates are represented in the same format.
    """
    text_blocks = page.get_text("dict", sort=True)["blocks"]

    # Determine the full page width
    page_width = page.rect.width
    page_height = page.rect.height

    if len(text_blocks)>0:
        header_text = text_blocks[0]  # Assuming header is the first block of text
        footer_text = text_blocks[-1]  # Assuming footer is the last block of text
     
        # Adjust header and footer coordinates to cover the entire page width
        header_coordinates = (0, 0, page_width, header_text["bbox"][3])
        footer_coordinates = (0, footer_text["bbox"][1], page_width, page_height)
    else:
        return [0, 0, page_width, 0], [0, page_height, page_width, page_height]
        
    return header_coordinates, footer_coordinates


def calculate_remaining_coordinates(header_coordinates: list, footer_coordinates: list):
    """
    Calculate the remaining coordinates of the page after excluding the header and footer.

    Args:
        header_coordinates (list): A list containing the coordinates of the header.
            The header coordinates are represented as [x0, y0, x1, y1],
            where (x0, y0) is the top-left corner and (x1, y1) is the bottom-right corner.
        footer_coordinates (list): A list containing the coordinates of the footer.
            The footer coordinates are represented in the same format as the header coordinates.

    Returns:
        tuple: A tuple containing the remaining coordinates of the page.
            The remaining coordinates are represented as (x0, y0, x1, y1),
            where (x0, y0) is the top-left corner and (x1, y1) is the bottom-right corner.
    """
    remaining_page = (header_coordinates[0], header_coordinates[3], footer_coordinates[2], 
                      footer_coordinates[1])

    return remaining_page

if __name__ == "__main__":
    print("Started")