# reDraw

Developed by David Reed and Jeremy Kemery

Version 3.1.2

[About reDraw](http://dave256apps.com/redraw)

Support email: [reDraw.app@gmail.com](mailto:reDraw.app@gmail.com?Subject=reDraw%20Support%20Version%203.1.2)

* Also see the help option on the Document Picker screen for help on it.

### What's new in Version 3.1.2:

* Minor UI tweaks

### What's new in Version 3.1.1:

* Small UI tweaks

### What's new in Version 3.1:

* Zooming/panning on iPad will also zoom/pan external screen.

* Long press next slide button will duplicate slide and move to it. Undo will delete the duplicated slide and move back to the original slide.

* Long press mark button will clear all marked points on the current slide. Undo will restore all the marked points.

### What's new in Version 3.0:

* Support for iOS 11 Files app and standard iOS 11 document picker so you may now store documents in iCloud Drive (note: not all Cloud providers such as Dropbox and Google Drive have been updated for proper support of creating/saving files). 

* Support for dragging images onto the canvas (before you had to copy and paste images and you may still use copy/paste if you prefer).

* Support for dragging PDFs from the Files app onto the canvas to import a PDF. You may still share a PDF from various PDF apps to reDraw.

### What's new in version 2.0:

* Full screen option in navigation bar.

* Share icon in navigation bar has record option. See [Recording](#Recording) help.

### What's new in version 1.2:

* Added a button in navigation bar (between + button for new slide and settings gear button) to expand the slide canvas. It hides the left bar and the the buttons/sliders above the canvas. Press it again to shrink the slide canvas and restore those views.

* Pressing !Cmd-/! on an externally connected keyboard will create a text drawable below the bottom item on the current slide no matter what drawing tool is currently selected.

* Added Previous/Next slide buttons on either side of slide number button. Pressing the slide number displays a view for picking any slide.

* When drawing with the Pen tool and the Shift button is On, lines that are nearly horizontal or nearly vertical are changed to horizontal or vertical lines.

* Long press the Select button to select all the objects on a slide.

---

## Pen/Line/Rect/Text drawing tools

Choose the drawing tool you want by tapping it and it remains active until you choose a different drawing tool.

The **Pen** tool allows you to do free hand drawing. Each stroke (from finger/pencil touch to finger/pencil raise) creates one *drawable* object in the timeline. When drawing with the Pen tool and the Shift button is On, lines that are nearly horizontal or nearly vertical are changed to horizontal or vertical lines.

The **Line** tool allows you to draw straight lines. When the **Shift** key is active, the straight lines are limited to horizontal or vertical lines. When using an Apple Pencil, you can create intermediate points on a multi-line segment by pressing firmly with the pencil at the point when you want to change the line direction. A multi-point line is consider one *drawable* in the timeline.

The **Rect** tool allows you to draw rectangles. When the **Shift** key is active, the shapes are squares. The touch down point is one of the corners of the rectangle and as you drag your finger/pencil, you can release it at the point where you want the diagonally opposite corner to be. Each rectangle is considered a separate *drawable* object. Rectangles are drawn as outlines and not filled in with a solid color.

The **Text** tool allows you to type text using the software virtual keyboard or a Bluetooth/Smart Keyboard. Tap the location where you want the top left of the text box to be and this will bring up the virtual keyboard (unless you have a hardware keyboard connected). Once the text box is shown, you may type the text you want with the keyboard. With the software keyboard, you may press the keyboard dismiss button (bottom right corner of the keyboard) to end the creation/editing of the *drawable* in the timeline. If you are using the hardware keyboard, press the **Text** tool button again to end creation/editing of the *drawable* in the timeline. When the **Text** tool is active, tapping on an existing Text object will begin editing it rather than creating a new *drawable* for the timeline. While editing text, use the blue handles on the blue outline rectangle to resize it. The red handle in the top middle allows you to move the Text.

While editing text with an external keyboard the following keyboard shortcuts may be used:

* !Cmd-/! (end editing of the text)
* !Cmd-Opt-/! (end editing of the text, set a stop point, and begin editing a new text object immediately below it)
* !Cmd-Opt-Shift-/! (end editing of the text, do NOT set a stop point, and begin editing a new text object immediately below it)
* If you are not currently editing text, pressing !Cmd-/! creates a new text object below the bottom object on the screen.

See the [Settings](#Settings) for how to change the font size for the Text.

---

## Undo/Redo

Just about every operation can be undone. Pressing the **Undo** button near the top left of the screen undoes the last operation (which could be adding a *drawable*, deleting a *drawable*, erasing the slide, changing the timeline slider, etc. The app supports multiple levels of undo. You may also redo the undone operations by pressing the **Redo** button that is next to the **Undo** button.

---

## Deleting/Erasing

You can delete the most recently drawn *drawable* object by pressing the delete button in the bottom left corner of the screen. You may move the timeline to change which object is the most recently drawn *drawable* affecting which one the delete button will delete. You may also use the Erase button in the top bar of the screen to delete multiple objects. It has options for the entire slide, from the current timeline position to the beginning or end of slide, or to the previous or next mark point. See [Slider Usage](#Timeline_Slider_Usage) for more information about mark points.

If you want to erase part of an object, draw over it using **Pen** tool with the color matching the background color of the slide (the default color is white and is not currently changeable). See [Pen/Line/Rect Styles](Pen/Line/Rect Styles) for how to change the style used when drawing. If you want to delete the entire object, use the delete button rather than drawing over top of it.

---

## Selecting objects

Activating the **Select** button puts the app in selection mode. You may draw a selection polygon around the *drawables* you want to select. Including any part of the *drawable* inside the selection polygon will include a *drawable* in the selected *drawables*. Once you finish drawing the selection polygon, the selection is drawn as a bounding rectangle but only the objects that were inside your polygon are selected. Selected objects are highlighted with a blue drop shadow. A Cut/Copy/Delete menu is shown if you selected any objects. Note that only visible items on the screen based on the timeline slider may be selected so you may need to move the timeline slider to the end if you want to select drawables that are not currently visible. In addition to choosing Cut/Copy/Delete, you can move the selected objects by dragging your finger/pencil starting the touch inside the selection rectangle and dragging to the new location. If you start the touch outside the selection rectangle, it allows you to select different objects.

You may resize existing selected drawables by placing two fingers inside the selection polygon and pinching/stretching your fingers to resize the selected objects. If the rectangle is too small to place your fingers inside it, activate the **Shift** button and then you may place your two fingers anywhere on the canvas to resize the selected objects.

Note, you may also select a single object by tapping on it. If the bounding rectangle for that object is the only bounding rectangle that your tap is inside, that single object will be selected.

After Cutting or Copying selected objects, you may Paste them at a new location on the canvas (or on a new page in the document or in a different reDraw document). You may also first change the slider timeline to affect where they appear in the timeline. If you have cut or copied objects and the **Select** button is still active, tapping on the screen will give you the option to paste the previously cut or copied objects.

Tapping a text *drawable* allows you to Cut, Copy, Delete, or Edit the text.

When non-text objects are selected, pressing one of the six style buttons see ([Pen/Line/Rect Styles](#Pen/Line/Rect_Styles)) changes the current style of the selected objects.

A long press of the Select button will select all the items on the current slide.

---

## Shift button

The **Shift** button affects how a number of tools work. As mentioned in the [Pen/Line/Rect Styles](#Pen/Line/Rect_Styles) section, when the **Shift** button is active, lines are limited to horizontal or vertical lines and rectangles are limited to squares. When objects are selected and the **Shift** button is active, pinching with two fingers anywhere on the canvas, resizes the selected objects. This is useful when the selected object(s) are too small to fit your fingers inside it (which will scale it even if the **Shift** button is inactive).

---

## Pen/Line/Rect Styles

There are six styles (the 6 circular buttons below the **Shift** button) that control the color and thickness when drawing with the **Pen**, **Line**, or **Rect** tool. You may change the color/thickness for any of these six styles by pressing and holding on one of the buttons. After a long tap on one of the six style buttons, a window appears that allows you to change the thickness and color using sliders. After you've changed the color/thickness, tap outside the window to make it disappear. Note that these six styles are saved with the document so different documents may have different styles stored with them. The white style can be used with the **Pen** or **Line** tool to erase part of an object by drawing over top of it. If you want to erase an entire object, delete it using the delete button (see [Deleting/Erasing](#Deleting/Erasing)).

---

## Pointer/Cursor

See the [Settings](#Settings) for how to make a pointer/cursor appear for pointing parts of the canvas out to people viewing a presentation with reDraw.

---

## Adding images and background images

If the app displaying an image supports dragging images out of it (such as Safari, the Photos app, etc.), you can drag an image and drop it onto the canvas. Previous versions of reDraw supported copying an image and then pasting it onto the canvas. That is still supported. You can add images to your document by copying an image from another source. Here are some ways to copy an image.

1. Use the Safari web browser to find your image, long tap on the image, and choose copy, and then return to your reDraw document.

2. Open your Photos app, find a photo, and press the Share icon button, choose Copy, and then return to your reDraw document.

3. Open the Mail app, long tap on a photo attachment, choose Copy, and then return to your reDraw document.

Once you've copied an image and are back on the slide in your reDraw document, make the **Select** tool active, and tap on the canvas and choose Paste.

You may choose to set a selected image as the background image for the current page (using the Set Slide Background Image option) or for all the pages in the document (using the Set Default Slide Background Image). See the [Settings](#Settings) section for how to delete a background image.

Selected images may be resized by using two fingers to pinch/stretch the image.

---

## Importing a PDF into reDraw

In version 3.0 and higher, you may drag a PDF from the Files app onto a slide to import a PDF and choose how many slides per PDF page to import.

You may also use the previous method for importing a PDF. Launch the app containing the PDF (such as GoodReader, PDF Expert, etc.). From that app, choose the option to share it, then choose the option to Open In, and select $Copy to reDraw$. This will switch to the reDraw app. If a document is already open, you are given the option to $Delete PDF$, $Import into different document$, or $Import into this document$. If a document is not already open, select the document into which you want to import the PDF or create a new document; the previously mentioned three options will be shown. If you do not want to import the PDF into any document, choose $Delete PDF$. If you want to import the PDF into a different document, choose that option; this will close the current document and then you can select the document you want to use. Once you have opened the document into which you want to import the PDF, choose the option to $Import into this document.$ You may also choose how many slides you want per PDF page. This is useful if you are importing a letter size PDF into a landscape document and want two sliders per PDF so you can show the top of the page on one slide and the bottom of the page on the next slide. It will import at the largest resolution that maintains the aspect ratio. If you import a letter size PDF into a 16:9 or 4:3 reDraw document, you will likely want to use the option to duplicate a slide and make multiple copies of each page or use the option to import multiple slides per page. Once you've done that, you can select the PDF object on a slide by using the $Select$ tool and then tapping the PDF. Once it is selected you can pinch/zoom and drag the PDF page until you get the portion you want visible on that slide. Repeat the process for the other slides.

After you have each PDF page scaled the way you want, you can use the pen, line, etc. tools to write on top of the PDF.

Note, PDFs may require a large amount of memory. Importing PDFs with 1-20 pages should work fine, but importing PDFs with hundreds of pages may cause the app to run out of memory. You may want to use another app (such as Preview on your Mac) to create a PDF with just a portion of the pages and then create separate reDraw documents for each portion of the original PDF document.

---

## Timeline Slider Usage

The timeline slider allows you to control what objects that you have drawn are currently visible on the canvas. This can be useful for presentations where you want to reveal part of the canvas in steps as you talk. Each object you draw causes a vertical line in the timeline slider representing that object. Once you have drawn multiple objects, you can tap a slider position to only draw the objects to that object or you may drag the circle that represents the current position to change position in the timeline. The black left and right arrows below the timeline slider on the right side allow fine control if you have so many drawables on a slide that it is difficult to select the exact position you want using your finger/pencil on the slider. Pressing these buttons move the timeline slider backward/forward one object at a time. 

The mark point button (between the two arrows) allows you to mark a point in the timeline that you want to stop at. Pressing it when the current position is already marked, unmarks that spot. The red arrow buttons move you to the previous/next marked point to make it easy to move to the correct next position when presenting. When you are at the end of a slide, pressing the next mark point button moves to the next slide. When you are at the beginning of a slide, pressing the previous mark point button moves to the previous slide. The play button in the top right corner of the screen just to the left of the Help button, moves to the beginning of the first slide for starting a presentation. The marked points are saved with the document so you can create a document with the points you want to stop at and then step through it later when presenting with the document.

Long pressing the mark point button will delete all the marked points on the current slide. If you accidentally do this, press the Undo button to restore the marked points.

---

## Zooming and Panning

Except when objects are selected and the **Shift** button is active, use two fingers to pinch/stretch to zoom in/out and drag two fingers to pan when you are zoomed in. Note that when you are at zoom level where the entire canvas is visible, dragging two fingers does not pan. If you have connected an external screen, the external screen will also zoom/pan as you zoom/pan the iPad canvas.

---

## Settings

Pressing the Settings button (gear icon near the top right of the screen) displays a Settings window. Tap outside the Settings window or press its **Done** button to make it disappear.

The Drawing Mode setting affects what touches in the canvas do. When in Pencil mode, only the pencil can be used to draw objects. A single finger will display a red circle for pointing objects out on the canvas except if you are in **Select** mode in which case a finger can be used to select objects or paste previously selected objects. In Finger mode, a single finger is used to draw objects. In Cursor mode, the finger or a pencil touch will draw the pointer circle. For all three modes, two fingers are used to pan or zoom (see [Zooming and Panning](#Zooming_and_Panning)).

The Grid Mode affects whether Lines (but not free form drawing in **Pen** mode), Rectangles, Text, and images snap to the nearest grid point. This is useful for lining up rectangles and snapping line endpoints to other lines or rectangles. Changing the grid size does not move existing objects so it is recommended that you pick a grid size for a document and do not change it once you've started drawing objects in the document.

The Mirror Display setting allows you to control what is seen on an external display (either an AirPlay screen or using the lightning adapter to connect an external monitor or projector). When Mirror Display setting is off, only the canvas is shown on the external screen (typically what you want for presenting a document). When the Mirror Display setting is on, the external monitor display matches the iPad screen. This is useful for demoing the app or necessary if you want to use multitasking to display two different apps side by side on the external screen. Note when using the iOS AirPlay option, you must select the AirPlay device you want the object to appear on and you must turn mirroring on in the AirPlay menu otherwise nothing will appear on the AirPlay device. You can then choose the option to mirror the display or just show the canvas using the reDraw Settings option to mirror the display.

If you have set a background image (see [Adding images and background images](#Adding_images_and_background_images)), the options to clear this slide's background image or the entire document's background image are active and may be pressed to delete the background image.

The Text Size affects the font for new text objects. You may also edit an existing text object, and open the Settings icon and use it to change the font size for that text object.

The Settings are not saved with a document and do not change when you open a different document (i.e., the settings stay in effect until you change them to a different value).

---

## External screen

Connecting an external screen either via AirPlay or an external monitor/projector via a lightning adapter allows you to present your document. See the [Settings](#Settings) section for mirroring options. When creating your document, it is recommended that you match the size or at least the aspect ratio of the external screen size you plan to use to avoid black bars on the sides or top/bottom that are necessary to preserve the aspect ratio.

---

## Pointer/Cursor

See the [Settings](#Settings) section for how to point out objects on an external screen without drawing as you point them out.

---

## Renaming the current document

Close the document and use the file picker to rename it. Long press the document and choose Rename.

---

## Reordering slides
Press the button labelled $Slide x of y$ in the middle below the slider to bring up a window that allows to select a different slide. Tap and hold a slide until it turns blue AND expands in size and then drag it to the position you want it among the other slides.

---

## Selecting/Duplicating a slide

Press the button labeled $Slide x of y$ in the middle below the slider to bring up a window that allows you to select a different slide. Tap the slide that you want to change to. Press the Edit button to delete or duplicate slides. After selecting one or more slides (selected slides are outlined in blue), press double rectangle with a plus button to duplicate these slides or press the trash can icon to delete those slides. Press the + button to add a new slide.

Press the arrow buttons on either side of the button labeled $Slide x of y$ to move to the previous/next slide. Long pressing the next slide button will duplicate the current slide and move to it.

---

## Exporting as PDF and Sharing a reDraw document

Press the share icon (square with an arrow pointing up). When exporting to PDF, the $New page at marked points$ switch determines whether there is one page per slide (when the switch is off) or a new page for every marked point in the slide. See the [Timeline Slider Usage](#Timeline_Slider_Usage) section for more information on marked points. Choosing $Share PDF$ allows you to email or AirDrop the PDF to recipients you specify in the new mail message dialog. Choosing $Open PDF in...$ allows you to create the PDF and open it in another app on your iPad that can view and/or edit PDFs.


To share it as reDraw document to be opened with reDraw on another iPad, use the document picker and long press on a file and choose the **Share** option or use the option to select multiple files and then press Share. See the Help option on the document picker screen for more information.

---

## Starting a presentation

Press the play button (just to the left of the Help button in the top right of the screen) to navigate to the beginning of the document to begin a presentation. Then use the next mark point button to step through your presentation. See [Timeline Slider Usage](#Timeline_Slider_Usage) for details on mark points.

----

## Recording

There are different techniques you can use to record a reDraw presentation. Starting with version 2.0, reDraw now supports recording directly on the iPad from within the app using Apple's ReplayKit framework. Note, due to iPad hardware limitations you cannot connect to an external display/projector using the Lightning to VGA or Lightning to HDMI adapters or use AirPlay at the same time as you are recording. Open your document, and choose the Share icon in the top navigation bar. An overlay view appears on top of your canvas (but the overlay window will not be in the recording). The overlay window can be moved by touching the gray portion at the top of the window and dragging it to the desired location.

Press the **Rec** button. A dialog requesting permission to record your screen and microphone (or the screen only) will appear (unless you had recently granted permission). If you only want to record the screen, choose the $Record Screen Only$ option. If you want to record your voice along with the screen choose the $Record Screen & Microphone$ option. You may use the built in microphone of the iPad or if you use Apple's lightning to USB adapter, you may be able to use a USB microphone. The developers have tested this and it works using their microphone if you also plug in a lightning cable to the adapter to supply power.

Unfortunately, ReplayKit does not always start recording immediately (usually it doesn't the first time you try to record during a session in our experience). We believe this is a bug and have reported it to Apple. But for now, if the recording has not immediately  we show another dialog letting you know this. Usually once you touch a button on the screen it does start recording so pressing the Ok button to dismiss the dialog starts the recording. You can tell that recording has started since the top of the overlay window will change from gray to red while it is recording. 

While it is recording you can use the buttons in the overlay window to move to the previous/next mark points. Pressing the Tools button expands the overlay window to show the different drawing modes and styles. If you have the Settings for your finger to act as a pointer, you can use your finger to position a red circle where you want to point, otherwise your finger can be used to draw. You may also draw with the Apple Pencil.

When you are done recording, press the **Stop** button (the **Rec** button changes to **Stop** while recording). You may then discard the recording or choose to view it. If you choose the view option, you may play the recording or crop the beginning and end using the timeline at the bottom. You can then use the Share icon in the top navigation bar to email it or use the **Save** button to save it to the camera roll.

The other options for recording are:

* connect the iPad to a Mac using a lightning to USB cable and use QuickTime to record the screen.

* use a third-party AirPlay server on your Mac such as **Reflector 2** or **Air Server** and use the iOS AirPlay option to display the iPad screen on your Mac and use **QuickTime Player** to record your Mac screen or use third party screen recording software such as **ScreenFlow** or **Camtasia for Mac** to record your Mac screen and then edit the recording.
