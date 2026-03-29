Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("D:\Users\dz\Desktop\website-A\shiny1-logo.png")
$bmp = New-Object System.Drawing.Bitmap($img)
$width = $bmp.Width
$height = $bmp.Height

$tx = $width - 150
$ty = $height - 150
$sampleColor = $bmp.GetPixel($tx, $ty)

$graphics = [System.Drawing.Graphics]::FromImage($bmp)
$brush = New-Object System.Drawing.SolidBrush($sampleColor)
$graphics.FillRectangle($brush, $width - 150, $height - 150, 150, 150)

$bmp.Save("D:\Users\dz\Desktop\website-A\shiny1-logo-clean.png", [System.Drawing.Imaging.ImageFormat]::Png)

$tl = $bmp.GetPixel(0,0)
$tr = $bmp.GetPixel($width-1, 0)
$bl = $bmp.GetPixel(0, $height-1)

Write-Host "Width: $width Height: $height"
Write-Host ("TopLeft: " + $tl.R + "," + $tl.G + "," + $tl.B)
Write-Host ("TopRight: " + $tr.R + "," + $tr.G + "," + $tr.B)
Write-Host ("BottomLeft: " + $bl.R + "," + $bl.G + "," + $bl.B)
Write-Host ("Sampled BG: " + $sampleColor.R + "," + $sampleColor.G + "," + $sampleColor.B)

$graphics.Dispose()
$brush.Dispose()
$bmp.Dispose()
$img.Dispose()
