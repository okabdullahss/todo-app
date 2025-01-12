
# PRECONDITIONS for overall automation startup

- Python is installed (in this case python 3.11) 
- Playwright is installed (settings -> interpreter -> playwright by Microsoft. Then run ''playwright install''  from terminal)
- pip install pytest-playwright 
- Verify all are installed by python --version / playwright --version via terminal

# Test Cases for TODO App

## 1. Add TODO Item
- **Description**: Verify that a user can add a new TODO item successfully.
- **Prerequisites**: Application is running.
- **Steps**:
  1. Open the application.
  2. Navigate to the TODO input field.
  3. Enter a valid TODO item (e.g., "Buy groceries").
  4. Click the "Add" button.
- **Validation**:
  - The new TODO item appears in the list.

## 2. View TODO Items
- **Description**: Verify that the user can view all added TODO items.
- **Prerequisites**: At least one TODO item exists.
- **Steps**:
  1. Open the application.
  2. Observe the list of TODO items.
- **Validation**:
  - All existing TODO items are displayed correctly.

## 3. Edit TODO Item
- **Description**: Verify that the user can edit an existing TODO item.
- **Prerequisites**: At least one TODO item exists.
- **Steps**:
  1. Open the application.
  2. Locate an existing TODO item.
  3. Click the "Edit" button.
  4. Modify the text (e.g., change "Buy groceries" to "Buy fruits").
  5. Save the changes.
- **Validation**:
  - The updated TODO item is displayed in the list.

## 4. Mark TODO as Done/Undone
- **Description**: Verify that the user can toggle the status of a TODO item.
- **Prerequisites**: At least one TODO item exists.
- **Steps**:
  1. Open the application.
  2. Locate an existing TODO item.
  3. Click the checkbox or toggle to mark the item as done.
  4. Optionally, click again to mark it as undone.
- **Validation**:
  - The item's status changes (e.g., strikethrough for done items).

## 5. Delete TODO Item
- **Description**: Verify that the user can delete an existing TODO item.
- **Prerequisites**: At least one TODO item exists.
- **Steps**:
  1. Open the application.
  2. Locate an existing TODO item.
  3. Click the "Delete" button.
  4. Confirm the deletion (if applicable).
- **Validation**:
  - The TODO item is removed from the list.
