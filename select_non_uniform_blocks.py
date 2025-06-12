
# Hao test 03 with gpt

import Rhino
import scriptcontext as sc

def select_non_uniformly_scaled_blocks():
    non_uniform_blocks = []
    tolerance = sc.doc.ModelAbsoluteTolerance

    # Iterate through all objects in the document
    for obj in sc.doc.Objects:
        # Check if the object is an instance object (block instance)
        if isinstance(obj, Rhino.DocObjects.InstanceObject):
            xform = obj.InstanceXform
            # print(xform)
            # Extract the basis vectors (columns) from the transformation matrix
            basis_x = Rhino.Geometry.Vector3d(xform.M00, xform.M10, xform.M20)
            basis_y = Rhino.Geometry.Vector3d(xform.M01, xform.M11, xform.M21)
            basis_z = Rhino.Geometry.Vector3d(xform.M02, xform.M12, xform.M22)
            # Compute the lengths (scaling factors)
            scale_x = basis_x.Length
            scale_y = basis_y.Length
            scale_z = basis_z.Length
            # Check if scaling factors are not equal within tolerance
            if not (Rhino.RhinoMath.EpsilonEquals(scale_x, scale_y, tolerance) and
                    Rhino.RhinoMath.EpsilonEquals(scale_y, scale_z, tolerance)):
                # Non-uniform scaling detected
                non_uniform_blocks.append(obj.Id)

    if non_uniform_blocks:
        # Unselect all objects
        sc.doc.Objects.UnselectAll()
        # Select the non-uniformly scaled block instances
        for obj_id in non_uniform_blocks:
            sc.doc.Objects.Select(obj_id)
        sc.doc.Views.Redraw()
        print("Selected {} non-uniformly scaled block instance(s).".format(len(non_uniform_blocks)))
    else:
        print("No non-uniformly scaled block instances found.")

if __name__ == "__main__":
    select_non_uniformly_scaled_blocks()
