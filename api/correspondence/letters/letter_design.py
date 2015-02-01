# -*- coding: utf-8 -*-
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus.tables import TableStyle


# Get the pre-defined styles and add custom styles
STYLES = getSampleStyleSheet()
STYLES.add(
        ParagraphStyle(
            name='ReturnAddress',
            parent=STYLES['Normal'],
            alignment=TA_RIGHT,
            fontSize=10,
        )
    )
STYLES.add(
        ParagraphStyle(
            name='DateLine',
            parent=STYLES['Normal'],
            spaceBefore=30*mm,
            fontSize=12,
        )
    )
STYLES.add(
        ParagraphStyle(
            name='LetterTitle',
            parent=STYLES['Normal'],
            spaceBefore=15*mm,
            fontName='Helvetica-Bold',
            fontSize=12,
        )
    )
STYLES.add(
        ParagraphStyle(
            name='Salutation',
            parent=STYLES['Normal'],
            spaceBefore=10*mm,
            spaceAfter=10*mm,
            fontSize=12,
        )
    )
STYLES.add(
        ParagraphStyle(
            name='LetterBody',
            parent=STYLES['Normal'],
            spaceAfter=3*mm,
            fontSize=12,
            leading=14,
        )
    )
STYLES.add(
        ParagraphStyle(
            name='Signature',
            parent=STYLES['Normal'],
            spaceBefore=23*mm,
            fontSize=12,
        )
    )
STYLES.add(
        ParagraphStyle(
            name='SignatoryTitle',
            parent=STYLES['Normal'],
            fontName='Helvetica-Bold',
            fontSize=12,
        )
    )
