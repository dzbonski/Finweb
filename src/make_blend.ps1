Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("D:\Users\dz\Desktop\website-A\shiny1-logo-clean.png")
$bmp = New-Object System.Drawing.Bitmap($img.Width, $img.Height)
$graphics = [System.Drawing.Graphics]::FromImage($bmp)

$ColorMatrix = New-Object System.Drawing.Imaging.ColorMatrix
$ColorMatrix.Matrix00 = 1.4
$ColorMatrix.Matrix11 = 1.4
$ColorMatrix.Matrix22 = 1.4
$ColorMatrix.Matrix40 = -0.18
$ColorMatrix.Matrix41 = -0.18
$ColorMatrix.Matrix42 = -0.18

$ImageAttributes = New-Object System.Drawing.Imaging.ImageAttributes
$ImageAttributes.SetColorMatrix($ColorMatrix)

$rect = New-Object System.Drawing.Rectangle(0, 0, $img.Width, $img.Height)
$graphics.DrawImage($img, $rect, 0, 0, $img.Width, $img.Height, [System.Drawing.GraphicsUnit]::Pixel, $ImageAttributes)

$bmp.Save("D:\Users\dz\Desktop\website-A\shiny1-logo-blend.png", [System.Drawing.Imaging.ImageFormat]::Png)

$graphics.Dispose()
$bmp.Dispose()
$img.Dispose()
