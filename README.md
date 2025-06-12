# Select Non-Uniformly Scaled Blocks in Rhino3D

Quickly identify and select all block instances that have been **non-uniformly scaled** in your model. This diagnostic script is essential for ensuring consistency in block usage, particularly before exporting, nesting, or collaborating across platforms where non-uniform scaling may cause issues.

## What Does the Script Do?

The **Select Non-Uniformly Scaled Blocks** tool:

* Scans all block instances (`InstanceObjects`) in the active Rhino model.
* Analyses the transformation matrix of each block to determine scaling along X, Y, and Z axes.
* Selects only those blocks where the scaling is not uniform (i.e., scaleX ≠ scaleY ≠ scaleZ within model tolerance).

This helps you catch and correct blocks that may appear visually correct but are geometrically distorted.

## Why Use It?

Non-uniform scaling of blocks can:

* Break definitions when blocks are exploded.
* Cause issues with exports (e.g., IFC, Revit, DWG).
* Introduce inconsistencies in fabrication, rendering, or detailing.

Use this tool to enforce block hygiene, especially in large collaborative or BIM-integrated models.

## How to Use the Script

### Load the Script in Rhino

**Method 1**:

1. Type `_RunPythonScript` in the Rhino command line.
2. Select the script file from your system.

### Method 2 Creating a Button or Alias (Optional)

#### Toolbar Button

1. **Right-click** a toolbar and choose **New Button**.
2. In the **Button Editor**:

   * **Left Button Command**:

     ```plaintext
     ! _-RunPythonScript "FullPathToYourScript\select_non_uniform_blocks.py"
     ```
   * **Tooltip**: `Select non-uniformly scaled block instances`.

#### Alias

1. Go to **Tools > Options > Aliases**.
2. Add a new alias:

   * **Alias**: `checkblocks`
   * **Command Macro**:

     ```plaintext
     _-RunPythonScript "FullPathToYourScript\select_non_uniform_blocks.py"
     ```

### Using the Tool

1. Run the script.
2. Rhino will:

   * Deselect everything.
   * Auto-select all non-uniformly scaled block instances.
   * Report the total count in the command line.

If none are found, you'll see a confirmation message instead.

## Technical Notes

* The script uses the **instance transformation matrix** to derive scaling vectors.
* Tolerance is based on `ModelAbsoluteTolerance`, ensuring robust comparison even at small scale.
* Only **block instances** are checked; block definitions or exploded geometry are not affected.
