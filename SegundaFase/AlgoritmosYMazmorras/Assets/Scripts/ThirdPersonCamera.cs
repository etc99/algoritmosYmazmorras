using UnityEngine;

public class ThirdPersonCamera : MonoBehaviour
{
    public Transform target; // The target (player) the camera will follow
    public float distance = 5.0f; // Distance from the target
    public float height = 2.0f; // Height above the target
    public float rotationSmoothTime = 0.12f; // Smooth time for camera rotation
    private Vector3 rotationSmoothVelocity;
    private Vector3 currentRotation;

    void LateUpdate()
    {
        // Camera rotation
        Vector3 targetRotation = new Vector3(0, target.eulerAngles.y, 0);
        currentRotation = Vector3.SmoothDamp(currentRotation, targetRotation, ref rotationSmoothVelocity, rotationSmoothTime);

        // Set camera rotation
        transform.eulerAngles = currentRotation;

        // Set camera position
        Vector3 position = target.position - (Quaternion.Euler(currentRotation) * Vector3.forward * distance) + Vector3.up * height;
        transform.position = position;
    }
}